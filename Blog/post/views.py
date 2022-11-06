from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
from datetime import date, datetime

# Create your views here.
def homePage(request: HttpRequest):
    posts = Post.objects.all().order_by('-id')[:5]
    context = {'post':posts}
    return render(request, 'post/home.html', context)

def showPosts(request: HttpRequest):
    posts = Post.objects.all()
    context = {'post':posts}
    return render(request, 'post/list.html', context)

def addPost(request: HttpRequest):
    date = datetime.isoformat(datetime.today(), timespec='minutes').replace('+',':')
    if request.method == 'POST':
        if 'is_published' in request.POST.keys():
            published = True
        else:
            published = False
        Post(title=request.POST['title'], content=request.POST['content'], is_published=published, publish_date=request.POST['publish_date']).save()
        return redirect('posts:list')
    return render(request, 'post/add.html', {'date':date})

def postDetail(request: HttpRequest, post_id: int):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'post/detail.html', context)

def updatePost(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        post.publish_date = datetime.isoformat(post.publish_date, timespec='hours').replace('+',':')
        if request.method == 'POST':
            if 'is_published' in request.POST.keys():
                published = True
            else:
                published = False
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.is_published = published
            post.publish_date = request.POST['publish_date']
            post.save()
            return redirect('post:list')
    except:
        return render(request, 'post/not_found.html')
    return render(request, 'post/update.html', {'post':post})

def deletePost(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
    except:
        return render(request, 'post/not_found.html')
    return redirect('post:list')

def searchPost(request: HttpRequest):
    search = request.GET.get('text', False)
    posts: dict = dict()
    if (search != False) and (len(search) > 0):
        posts = Post.objects.filter(content__contains=search)
    context = {'post':posts}
    return render(request, 'post/search.html', context)
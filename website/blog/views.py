from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from . models import Post
# Create your views here.

def posts (request:HttpRequest):

    if request.method =="POST":
        new_post = Post(title=request.POST["title"],content=request.POST["content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_post.save()
    return render(request, 'blog/posts.html') 

def preview (request:HttpRequest):
    posts_list = Post.objects.all()
    
    return render(request, 'blog/preview.html',{"posts_list": posts_list })   

def post_detail(request : HttpRequest, post_id : int
):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/notFound.html")

    return render(request, "blog/details.html", {"posts_list": posts_list })

def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/notFound.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("blog:posts_list")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blog/update.html", {"post" : post})

def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/notFound.html")

    post.delete()

    return redirect("blog:posts_list")

def search_post(request: HttpRequest):
    search = request.GET.get('text', False)
    posts: dict = dict()
    if (search != False) and (len(search) > 0):
        posts = Post.objects.filter(content__contains=search)
    context = {'posts':posts}
    return render(request, 'blog/search.html', context)
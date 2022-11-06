from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.


def post_add(request : HttpRequest):
    
    if request.method == 'POST':
        
        new_post = Post(title = request.POST['title'], content = request.POST['content'],is_published = request.POST['is_published'], date = request.POST['date'])

        new_post.save()

    return render(request, 'new_post.html')



def posts(request : HttpRequest):

    posts = Post.objects.all()

    return render(request,'index.html',{'posts' : posts} )



def post_d(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id = post_id)
    except:
        return render(request,'not_found.html')

    return render(request,'post_d.html',{'post' : post})
    pass



def up_post(request : HttpRequest, po):

    return render(request,'up_post.html' , {'post ' : ""})
    pass



def del_post(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        render(request,'not_found.html')
    post = post.delete()
    return redirect('posts')
    






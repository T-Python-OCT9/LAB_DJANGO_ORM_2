import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from datetime import date
# HttpResponse
# Create your views here.

#Users can read the blog posts.

def home(request: HttpRequest):
    posts_all = Post.objects.all()
    return render(request, "Blog_app/home.html", {"posts": posts_all})

#- Add search input , to let user search for posts based on title (filter).

def search_posts(request: HttpRequest):
    try:
        if request.method=='GET':
            search_title =request.GET.get('search')
            search_posts =Post.objects.filter(Title= search_title)
    except:
        return render(request, "Blog_app/not_found.html")

    return render(request, "Blog_app/search.html", {"search_posts":search_posts})

# Users can Add a blog post.

def add_blog(request: HttpRequest):
    if request.method == "POST":
        posts = Post(
            Title=request.POST["Title"],
            Content=request.POST["Content"],
            is_published=True if "is_published" in request.POST else False,
            publish_date=request.POST.get('publish_date'))
        posts.save()
        return redirect("Blog_app:home")

    return render(request, "Blog_app/add_blog.html")


#- Add update post page.

def update_post(request: HttpRequest, post_id: int):

    try:
        post = Post.objects.get(id=post_id)

    except:
        return render(request, "Blog_app/not_found.html")
        

    if request.method == "POST":
        post.Title = request.POST["Title"]
        post.Content = request.POST["Content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("Blog_app:home")
    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")

    
    return render(request, "Blog_app/update_post.html", {"post": post})


#- Add detail page for posts.

def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Blog_app/not_found.html")

    return render(request, "Blog_app/post.html", {"post" : post})


#- Add delete post.

def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Blog_app/not_found.html")

    post.delete()

    return redirect("Blog_app:home")
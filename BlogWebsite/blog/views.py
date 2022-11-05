from django.shortcuts import redirect, render
from django.http import HttpRequest ,HttpResponse
from .models import *

# Create your views here.

def home(request :HttpRequest):
    return render(request  , "blogs/home.html")


def update (request :HttpRequest , post_id :int):
    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blogs/not_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("blog:read_blog_post")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blogs/update.html", {"blog" : post})



def delete(request :HttpRequest , post_id :int):
    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blogs/not_found.html")

    post.delete()
    return redirect("blog:read_blog_post")



def read_blog_post(request :HttpRequest):
    view_blogs = Blog.objects.all()
  
    return render(request  , "blogs/read_blog.html" , {"blogs" : view_blogs})



def add_blog_post (request :HttpRequest):
     if request.method == "POST":
        new_blog = Blog(title = request.POST ["title"] , content = request.POST ["content"] ,is_published = request.POST["is_published"] ,publish_date = request.POST["publish_date"] )
        new_blog.save()
        return redirect("blog:read_blog_post")
     return render(request , "blogs/add_blog.html")
     



def details_post(request :HttpRequest , post_id : int):
    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blogs/not_found.html")

    return render(request , "blogs/detail_post.html" , {"blog" : post})


def search(request : HttpRequest , search_post :str):
   try:
      request.method == 'GET'
      search_post = Blog.objects.filter(title__contains = ["title"])
      search_post ==['search']
   except:
        return render(request , "blogs/not_found.html")

   return render(request , "blogs/detail_post.html" , {"blog" : search_post})

    

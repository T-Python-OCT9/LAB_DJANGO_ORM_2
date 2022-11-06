from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
from .models import Blog 
# اسوي امبورت للكومنت 
# Create your views here.


def add_blog (request: HttpRequest):

    if request.method == "POST":
        
        newBlog= Blog(Title=request.POST["Title"] , Content=request.POST["Content"], is_published=request.POST["is_published"], publish_date= request.POST["publish_date"])
        newBlog.save()
    return render(request,"blog/add_blog.html")# اسم الملف 


def all_post (request :HttpRequest):

    if "search" in request.GET:
        posts = Blog.objects.filter(title__contains=request.GET["search"])
    else:
        allPosts = Blog.objects.all()


    return render(request , "blog/show_post.html", {"Post": allPosts}) 


def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blog/not_found.html")

    return render(request, "blog/post_detail.html", {"post" : post})


def update_post(request: HttpRequest, post_id:int):

    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blog/not_found.html")

    if request.method == "POST":
        Blog.Title = request.POST["title"]
        Blog.Content = request.POST["content"]
        Blog.publish_date = request.POST["publish_date"]
        Blog.is_published = request.POST["is_published"]
        Blog.save()

        return redirect("blog:all_post")

    Blog.publish_date = Blog.publish_date.isoformat("T", "hours").replace("+", ":") 
    return render(request, "blog/update_post.html", {"post" : post})

def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Blog.objects.get(id=post_id)
    except:
        return render(request , "blog/not_found.html")

    Blog.delete()

    return redirect("blog:all_post ")



def add_commint(request :HttpRequest , post):
    pass
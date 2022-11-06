from audioop import reverse
from datetime import date
import datetime
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from .models import Blog

# Create your views here.

def home(request:HttpRequest):
    if 'search' in request.GET:
        blogs = Blog.objects.filter(title__contains = request.GET['search'] )
    else:
        blogs = Blog.objects.all()
    context={"blog" : blogs}
    return render(request, "app1/blog1.html" , context )


def add_blog(request:HttpRequest):
    if request.method == "POST":
        new_blog= Blog(title=request.POST["title"], description= request.POST["description"],is_published=True, publish_date=date.today() )
        new_blog.save()

    return render(request, "app1/addblog.html")

def Blog_D(request : HttpRequest, Blog_id : int):

    try:
        blog = Blog.objects.get(id=Blog_id)
    except:
        print("not found")

    return render(request, "app1/Blog_D.html", {"Blog" : blog})


def update_Blog(request: HttpRequest, Blog_id:int):

    try:
        blog= Blog.objects.get(id=Blog_id)
    except:
        print("not found ")

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.description = request.POST["description"]
        blog.is_published=True
        blog.publish_date=date.today()
        blog.save()
        return redirect("http://127.0.0.1:8000/app1/home/")
    return render(request, "app1/update_Blog.html", {"Blog" : blog})


def delete_Blog(request: HttpRequest, Blog_id:int):

    try:
        blog = Blog.objects.get(id=Blog_id)
    except:
        print("not found ")

    blog.delete()

    return redirect("http://127.0.0.1:8000/app1/home/")



def Blog_D(request : HttpRequest, Blog_id : int):

    try:
        blog = Blog.objects.get(id=Blog_id)
    except:
        print("not found")

    return render(request, "app1/Blog_D.html", {"Blog" : blog})









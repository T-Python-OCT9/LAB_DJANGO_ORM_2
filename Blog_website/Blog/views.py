from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog_Data

# Create your views here.

def home(request:HttpRequest):
    return render(request, "Blog/home.html")


def read_blog(request:HttpRequest):
    msg_list = Blog_Data.objects.all()
    return render(request, "Blog/read_blog.html", {"msg_list" : msg_list})
    

def add_blog(request: HttpRequest):

    if request.method == "POST":
        new_msg = Blog_Data(Title=request.POST["Title"], Content= request.POST["Content"],is_published =request.POST["is_published"] ,publish_date= request.POST["publish_date"])
        new_msg.save()
        return redirect("Blog:read")


    return render(request, "Blog/add_blog.html")


def blog_detail(request:HttpRequest , blog_id = int ):
    try:
        Blog = Blog_Data.objects.get(id=blog_id)
    except:
        return render(request , "Blog/not_found.html")
    return render(request, "Blog/detail.html" , {"Blog":Blog})


def update_blog(request:HttpRequest , blog_id = int ):
    try:
        Blog = Blog_Data.objects.get(id=blog_id)
    except:
        return render(request , "Blog/not_found.html")
    if request.method == "POST":
        Blog.Title = request.POST["Title"]
        Blog.Content = request.POST["Content"]
        Blog.publish_date = request.POST["publish_date"]
        Blog.is_published = request.POST["is_published"]
        Blog.save()

        return redirect("Blog:read")
      
    return render(request, "Blog/update.html"  , {"Blog":Blog})


def delete_blog(request:HttpRequest , blog_id:int):
    try:
        Blog = Blog_Data.objects.get(id=blog_id)
    except:
        return render(request , "Blog/not_found.html")
    
    Blog.delete()
    return redirect("Blog:read")


def search(request:HttpRequest):
    return render(request, "Blog/search.html")


def not_found(request:HttpRequest):
    return render(request, "Blog/not_found.html")
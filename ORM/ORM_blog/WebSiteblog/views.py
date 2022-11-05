from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from datetime import datetime



def home(request: HttpRequest):
    post = Post.objects.filter(is_published=True)
    return render(request, "WebSiteblog/index.html", {"posts" : post})

def post_list(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "WebSiteblog/all_posts.html", {"posts" : posts})

def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "WebSiteblog/not_found.html")

    return render(request, "WebSiteblog/post_detail.html", {"post" : post})


def add_post(request:HttpRequest):

    if request.method == "POST":
        new_post = Post(post_title=request.POST["post_title"],post_content=request.POST["post_content"], publish_date=request.POST["publish_date"],author_name=request.POST["author_name"] ,is_published=request.POST["is_published"])
        new_post.save()
        
     
    return render(request, "WebSiteblog/add_post.html")

def update_post(request: HttpRequest, post_id:int):

    try:
        posts = Post.objects.get(id=post_id)
        posts.publish_date = posts.publish_date.isoformat("T", "hours").replace("+", ":")
        if request.method == "POST":
            posts.post_title = request.POST["post_title"]
            posts.post_content = request.POST["post_content"]
            posts.publish_date = request.POST["publish_date"]
            posts.author_name = request.POST["author_name"]
            posts.is_published = request.POST["is_published"]
            posts.save()
            return redirect("WebSiteblog:post_list")                   
    except:
        return render(request , "WebSiteblog/not_found.html")
    return render(request, "WebSiteblog/update_post.html", {"posts" : posts})


def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
        
        
    except:
        return render(request , "WebSiteblog/not_found.html")
    post.delete()
    return redirect("WebSiteblog:post_list")
    
def search_title(request:HttpRequest):
    
    try:
        if request.method=='POST':
            searched=request.POST["searched"]
            posts=Post.objects.filter(post_title__contains = searched)
    except:
        return render(request , "WebSiteblog/not_found.html")
    
    return render(request,"WebSiteblog/search.html",{"searched":searched ,"posts":posts})


    

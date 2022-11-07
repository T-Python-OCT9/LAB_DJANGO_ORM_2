from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post


def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"])
        new_post.save()
    return render(request, "blog/add_post.html")



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/Not_Found.html")

    return render(request, "blog/post_detail.html", {"post" : post})


def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/Not_Found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("blogApp:list_posts")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blog/update_post.html", {"post" : post})

def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/not_found.html")

    post.delete()

    return redirect("blog:list_posts")

def list_posts(request: HttpRequest):

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()
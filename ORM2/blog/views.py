from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"])
        new_post.save()


    return render(request, "blog/addpost.html")



def list_posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "blog/viewpost.html", {"posts" : posts})





def update_post(request: HttpRequest, post_id:int):

    pass


def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blog/not_found.html")

    post.delete()

    return redirect("blog:list_posts")
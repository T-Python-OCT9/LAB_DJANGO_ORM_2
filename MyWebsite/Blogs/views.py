from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"])
        new_post.save()


    return render(request, "Blogs/addposts.html")



def list_posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "Blogs/show.html", {"posts" : posts})



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Blogs/none_found.html")

    return render(request, "Blogs/post_detail.html", {"post" : post})


#update post
def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Blogs/none_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("Blogs:list_posts")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "Blogs/updated_posts.html", {"post" : post})


#delete post
def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Blogs/none_found.html")

    post.delete()

    return redirect("Blogs:list_posts")

def Search_posts(request:HttpRequest):
    if request.method == "GET":
        title = request.GET.get('search')
        post = Post.objects.filter(title__contains = title)

    
    return render(request, "Blogs/show.html", {"Search_posts" : post} )
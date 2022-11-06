from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Post
# Create your views here.

def add_post(request:HttpRequest):
    if request.method == "POST":
        new_blog = Post(title=request.POST.get('title'), content= request.POST.get('content'),is_published = request.POST.get('is_published') ,publish_date= request.POST.get('publish_date'))
        new_blog.save()

        return redirect("mrAhmad")


    return render(request, "mrAhmad/")


def list_post(request:HttpRequest):
    all_post = Post.objects.all()
    context = {'all_post': all_post}
    return render(request, "mrAhmad/list_post.html", context)


def viwe_post(request:HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request, "mrAhmad/not_found.html")
    else:
        context = {'post': post}
        return render(request, "mrAhmad/view.html", context)

def update_post(request:HttpRequest, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request, "mrAhmad/not_found.html")
    else:
        if request.method == 'POST':
            print(request.POST)
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.publish_date = request.POST.get('publish_date')
            post.is_published = request.POST.get('is_published')
            post.save()

            return redirect("mrAhmad:list_post")

        post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
        return render(request, "mrAhmad/upd.html",{'post': post})


def delete_post(request:HttpRequest, post_id:int):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request, "mrAhmad/not_found.html")
    else:
        post.delete()
        return redirect("mrAhmad:list_post")


def search(request:HttpRequest):
    if request.method == "GET":
        title = request.GET.get('search')
        post = Post.objects.filter(title__contains = title)

    context = {'all_post': post}
    return render(request, "mrAhmad/list_post.html", context)
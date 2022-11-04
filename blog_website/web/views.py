from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blogPost
from django.db.models import Q


# Create your views here.


def home_page(request):

    return render(request, "base.html")

def read_post(request : HttpRequest):
    post_list = blogPost.objects.all()

    return render(request, "readPost.html", {"posts": post_list})


        
def add_post(request: HttpRequest):

    if request.method == "POST":
        new_post = blogPost(title=request.POST["title"], content= request.POST["content"], publish_date=request.POST["publish_date"], is_published=request.POST["is_published"])
        new_post.save()
        return redirect("web:read_post")

    return render(request, "addPost.html")



def post_detail(request: HttpRequest, post_id : int):

    try:
        post = blogPost.objects.get(pk=post_id)

    except:
        return render(request, "not_found.html")

    return render(request, "postDetail.html", {"post": post})


def delete_post(request: HttpRequest, post_id : int):

    try:
        post = blogPost.objects.get(pk=post_id)

    except:
        return render(request, "not_found.html")

    post.delete()

    return redirect("web:read_post")



def update_post(request: HttpRequest, post_id: int):
        
    try:
        post = blogPost.objects.get(pk=post_id)
    
    except:
        return render(request, "not_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("web:read_post")
    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "updatePost.html", {"post": post})


def searchPost(request: HttpRequest):

    if request.method == "GET":
        query = request.GET.get("q")

        submitbutton = request.GET.get("submit")
        if query is not None:
            lookups= Q(title__icontains = query) | Q(content__icontains = query)
            results = blogPost.objects.filter(lookups).distinct()
            context = {"results": results, "submitbutton": submitbutton}

            return render(request, "search.html", context)
        else:
            return render(request, "search.html" )
    else:
        return render(request, "search.html" )
        
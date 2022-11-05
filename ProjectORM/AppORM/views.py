
from django.shortcuts import  render,redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
from datetime import date
from .models import Post


# ------------ HOME PAGE -----------------
def home(request: HttpRequest):
    return render(request , "AppORM/base.html")



# ------------ CREATE NEW BLOG -----------------
def add_blog(request: HttpRequest):
    if request.method == "POST":

        new_blog = Post(
            title=request.POST["title"],
            content= request.POST["content"],
            # is_published= True if "is_published" in request.POST else False,
            publish_date= request.POST["publish_date"],
            is_published=request.POST["is_published"],
            )
            
        new_blog.save()
    return render(request, "AppORM/add_blog.html")

# ------------ All BLOGS PAGE -----------------
def all_blogs(request:HttpRequest):
    blogs_list = Post.objects.all()[:10]
    return render(request, "AppORM/list_blogs.html", {"blogs" : blogs_list})

# ------------  BLOG DETAILS PAGE -----------------
def blog_detail(request:HttpRequest , blog_id : int):
    try:
        blog_detail= Post.objects.get(id=blog_id)
    except:
        return render(request, "AppORM/not_found.html")

    return render(request, "AppORM/blog_detail.html", {"blogs" : blog_detail})

# ------------ UPDATE BLOGS PAGE -----------------
def update_blog(request:HttpRequest , blog_id : int):
    try:
        blog= Post.objects.get(id=blog_id)
    except:
        return render(request, "AppORM/not_found.html")
    
    if request.method == "POST":
        blog.title =request.POST["title"]
        blog.content= request.POST["content"]
        blog.publish_date= request.POST["publish_date"]
        blog.is_published= request.POST["is_published"]
        blog.save()
        return redirect("AppORM:all_blogs")
    blog.publish_date = blog.publish_date.isoformat("T","hours").replace("+",":")
    return render(request, "AppORM/update_blog.html", {"blogs" : blog})

# ------------ DELETE BLOG -----------------
def delete_blog(request:HttpRequest , blog_id : int):
    try:
        blog= Post.objects.get(id=blog_id)
    except:
        return render(request, "AppORM/not_found.html")
    blog.delete()
    return redirect("AppORM:all_blogs")


# ------------ SEARCH BLOG -----------------
def search_blog(request: HttpRequest): 
    if request.method == "POST":
        searched = request.POST['searched']
        blog = Post.objects.filter(title__contains=searched)
        return render(request, "AppORM/searchd_posts.html", { "searched" : searched,"blogs" : blog})
    else:
        return render(request, "AppORM/searchd_posts.html", {})
    



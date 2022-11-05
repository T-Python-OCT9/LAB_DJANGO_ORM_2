from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Fun_blog
from datetime import date

# Create your views here.

def fun_post(request: HttpRequest):
  
    if request.method == "POST":
        Add_blog = Fun_blog(Title=request.POST["Title"], Content= request.POST["Content"], is_published= request.POST["is_published"],  publish_date= request.POST["publish_date"])
        Add_blog.save()
    
      
    return render(request, "blog/post.html") 



def all_blogs(request:HttpRequest):
    list = Fun_blog.objects.all()

    return render(request, "blog/read.html", {"ALL_BLOGS" : list}) 


def post_detail(request : HttpRequest, post_id : int):

    
        post = Fun_blog.objects.get(id=post_id)
   

        return render(request, "blog/details.html", {"post" : post})  



def update_post(request: HttpRequest, post_id:int):

   
        post = Fun_blog.objects.get(id=post_id)
    

        if request.method == "POST":
          post.Title = request.POST["Title"]
          post.Content = request.POST["Content"]
          post.publish_date = request.POST["publish_date"]
          post.is_published = request.POST["is_published"]
          post.save()
          return redirect("blog:all_blogs")

        return render(request, "blog/update.html", {"post" : post})     


def delete_post(request: HttpRequest, post_id:int):


        post = Fun_blog.objects.get(id=post_id)

        post.delete()

        return redirect("blog:all_blogs")  

        

def fun_filter(request: HttpRequest, post_title):


        post = Fun_blog.objects.filter(Title = post_title)

        return render(request, "blog/read.html", {"post" : post})         
         


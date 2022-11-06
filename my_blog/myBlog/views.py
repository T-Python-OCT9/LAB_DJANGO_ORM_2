from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post


# Create your views here.


def base(request : HttpRequest):
  return render(request, 'base.html')

def base1(request : HttpRequest):
  return render(request, 'base1.html')

def add_posts(request : HttpRequest):
  if request.method == "POST":
    new_post = Post(Title=request.POST['Title'], Content = request.POST["Content"], publish_date = request.POST['publish_date'], is_published = request.POST['is_published'])
    new_post.save()

  return render (request, 'post.html')
#list posts
def read(request : HttpRequest):
  all_posts = Post.objects.all()
  return render (request , 'read.html', {'Posts' : all_posts})

'''def read(request: HttpRequest):
    posts = Post.objects.all()
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "view_posts.html", {"posts" : posts})'''





def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    return render(request, "post_detail.html", {"post" : post}) 




#update post
def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    if request.method == "POST":
        post.Title = request.POST["title"]
        post.Content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("my_blog:read_post")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "update_post.html", {"post" : post})

#delete post
def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    post.delete()

    return redirect("my_blog:read_post")

def search(request : HttpRequest , input:str):

    try:
      result =Post.objects.filter(name=input)
      
    except:
        return render(request , "not_found.html")

    return render (request, 'search_results.html', result)




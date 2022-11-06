from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_post(request):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"])
        new_post.save()


    return render(request, "blogApp/add_post.html")



def list_posts(request: HttpRequest):
    posts = Post.objects.all()
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "blogApp/view_posts.html", {"posts" : posts})



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    return render(request, "blogApp/post_detail.html", {"post" : post})


#update post
def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("blogApp:list_posts")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blogApp/update_post.html", {"post" : post})


#delete post
def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    post.delete()

    return redirect("blogApp:list_posts")






def search_post(request: HttpRequest):
    search = request.GET.get('text', False)
    posts: dict = dict()
    if (search != False) and (len(search) > 0):
        posts = Post.objects.filter(content__contains=search)
    context = {'posts':posts}
    return render(request, 'blogApp/search.html', context)
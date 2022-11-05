from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from.models import Blog




def blog (request:HttpRequest):

    return render(request,'blogApp/blog.html')



def blogAdd (request:HttpRequest):
    if request.method=="POST":
        
        new_blog= Blog(title=request.POST["title"], content=request.POST["content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()
    return render(request,'blogApp/blogAdd.html')




def blogRead (request:HttpRequest):
    blog_list=Blog.objects.all()
    if request.method=="POST":
        blog_list=Blog.objects.filter(title__contains = request.POST["search"])


#posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request,'blogApp/blogRead.html',{"blogs":blog_list})


def view_info(request:HttpRequest,post_id : int):
   

    view_info=Blog.objects.get(id=post_id)

    return render(request,'blogApp/blogView.html',{"postView":view_info})




def delete(request:HttpRequest,post_id : int):
    view_info=Blog.objects.get(id=post_id)
    view_info.delete()
    return render(request,'blogApp/blogRead.html')





def update(request:HttpRequest,post_id : int):
    try:
        view_info=Blog.objects.get(id=post_id)
    except:
        return render(request, "blogApp/notFound.html")

    if request.method == "POST":
        view_info.title = request.POST["title"]
        view_info.content = request.POST["content"]
        view_info.publish_date = request.POST["publish_date"]
        view_info.is_published = request.POST["is_published"]
        view_info.save()

        return redirect("blogApp:Read")

    view_info.publish_date = view_info.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blogApp/update_post.html", {"blogs" : view_info})



# Create your views here.


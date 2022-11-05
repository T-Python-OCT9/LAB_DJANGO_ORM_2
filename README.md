# LAB_DJANGO_ORM_2

## using your previous LAB "LAB_DJANGO_ORM_1" , do the following:
- Add detail page for posts.
- Add update post page.
- Add delete post.
- Add search input , to let user search for posts based on title (filter).


<a href="{% url 'blogApp:delete' postView.id %}">Delete</a>



<a  href="{% url 'blogApp:view_info' blog.id %}" class="btn btn-dark stretched-link ">Views</a>



{% url 'blogApp:delete' postView.id %}




def delete(request:HttpRequest,post_id : int):
   

    view_info=Blog.objects.get(id=post_id)
    view_info.delete()

    return redirect("blogApp:blog")



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




    <a href="{% url 'blogApp:update' blog.id%}" class="btn btn-secondary stretched-link">update</a>




      path("view/<post_id>", views.delete, name="delete"),
    path("update/<post_id>",views.update, name="update")




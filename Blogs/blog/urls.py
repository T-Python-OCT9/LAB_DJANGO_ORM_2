from django.urls import path
from . import views

app_name = "Blogs"

urlpatterns = [
    
    path("post/", views.fun_post, name="post"),
    
    path("AllBlogs/", views.all_blogs, name="AllBlogs"),
    
    path("update/<post_id>/", views.update_post, name="update"),

    path("delete/<post_id>/", views.delete_post, name="delete_post"), 

    path("f/<post_id>/", views.fun_filter, name="filter"),
]
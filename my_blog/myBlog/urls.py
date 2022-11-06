from django.urls import path 
from . import views

app_name = "my_blog"

urlpatterns = [
path("base/", views.base, name="home"),
path("post/", views.add_posts, name="add_post"),
path("read/", views.read, name="read_post"),
path("base1/", views.base1, name="base"),
path("post_detail/<post_id>", views.post_detail, name="post_detail"),
path("update_post/<post_id>", views.update_post, name="update_post"),
path("delete/<post_id>/", views.delete_post, name="delete_post"),
path("search_results/", views.search, name="search"),

]

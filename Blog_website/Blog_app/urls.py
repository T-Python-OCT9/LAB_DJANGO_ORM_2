from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "Blog_app"


urlpatterns = [
    path('home', views.home, name="home"),
    path('add_blog', views.add_blog, name="add_blog"),
    path("search/", views.search_posts, name="search_posts"),
    path("post/update/<post_id>/", views.update_post, name="update_post"),
    path("post/detail/<post_id>/", views.post_detail, name="post_detail"),
    path("post/delete/<post_id>/", views.delete_post, name="delete_post"),
]

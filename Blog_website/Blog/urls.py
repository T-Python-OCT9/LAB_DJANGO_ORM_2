from django.urls import path
from . import views


app_name = "Blog"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("read/", views.read_blog, name="read"),
    path("add/", views.add_blog, name="add"),
    path("search/", views.search, name="search"),
    path("search_data/", views.search_data, name="search_data"),
    path("404/", views.not_found, name="not_found"),
    path("detail/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("update/<blog_id>/", views.update_blog, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),    
]
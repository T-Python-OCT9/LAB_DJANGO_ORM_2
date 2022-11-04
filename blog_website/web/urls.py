from django.urls import path
from . import views


app_name = "web"


urlpatterns = [

    path("", views.home_page, name="home_page"),

    path("add/", views.add_post, name="add_post"),

    path("read/", views.read_post, name="read_post"),

    path("detail/<post_id>/", views.post_detail, name="post_detail"),

    path("update/<post_id>", views.update_post, name="update_post"),

    path("delete/<post_id>", views.delete_post, name="delete_post"),

    path("search/", views.searchPost, name="search_post"),


]
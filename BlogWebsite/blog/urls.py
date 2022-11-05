from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("home/" , views.home , name="home"),
    path("add/", views.add_blog_post, name = "add_blog_post"),
    path("read/", views.read_blog_post, name="read_blog_post"),
    path("detail/<post_id>" , views.details_post , name="details_post"),
    path("update/<post_id>" , views.update , name="update"),
    path("delete/<post_id>" , views.delete , name="delete"),
    path("search/<title> " , views.search , name="search")

]
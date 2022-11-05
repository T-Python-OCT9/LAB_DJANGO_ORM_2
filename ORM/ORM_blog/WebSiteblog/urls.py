from django.urls import path
from . import views

app_name = "WebSiteblog"

urlpatterns = [
    
    path("home/", views.home, name="home"),
    path("add/", views.add_post , name="add_post" ),
    path("list/" , views.post_list , name="post_list"),
    path("detail/<post_id>/" , views.post_detail ,name="post_detail"),
    path("update/<post_id>/" ,views.update_post ,name="update_post"),
    path("delete/<post_id>/" ,views.delete_post , name="delete_post"),
    path("search/" , views.search_title , name="search-title"),
]
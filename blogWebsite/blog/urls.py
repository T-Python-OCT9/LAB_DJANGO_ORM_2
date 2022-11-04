from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [   
    path("", views.add_post, name="add_post"),
    path("posts/", views.list_post, name="list_post"),
    path("view/<int:post_id>/", views.viwe_post, name="view_post"),
    path("update/<int:post_id>/", views.update_post, name="update_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("search/", views.search, name="search"),
]
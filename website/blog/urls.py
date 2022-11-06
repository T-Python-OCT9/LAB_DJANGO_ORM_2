from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("posts/", views.posts, name = "posts"),
    path("preview/",views.preview, name = "preview"),
    path("posts/detail/<post_id>/", views.post_detail, name="detail"),
    path("posts/update/<post_id>/", views.update_post, name="update"),
    path("posts/delete/<post_id>/", views.delete_post, name="delete"),
    path("posts/search/",views.search_post,name="search")

]

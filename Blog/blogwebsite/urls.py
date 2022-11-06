from django.urls import path
from . import views

app_name = "Blogs"

urlpatterns = [
    path('add/', views.add_new_blog, name = "Add"),
    path('Home/', views.add_new_blog, name = "base"),
    path("style/", views.set_style, name="set_style"),
    path("list/", views.blogs_list, name="blogs_list"),
    path("detail/<post_id>/", views.post_detail, name="post_detail"),
    
]
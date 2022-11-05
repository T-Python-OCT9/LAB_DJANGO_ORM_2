from django.urls import path
from . import views

app_name = "AppORM"

urlpatterns = [
    path('', views.home , name="home"),
    path('add_blog', views.add_blog , name="add_blog"),
    path('all_blogs', views.all_blogs , name="all_blogs"),
    path('blog_detail/<blog_id>/', views.blog_detail , name="blog_detail"),
    path('update_blog/<blog_id>/', views.update_blog , name="update_blog"),
    path('delete_blog/<blog_id>/', views.delete_blog , name="delete_blog"),
    path('search_blog', views.search_blog , name="search_blog"),
    
]

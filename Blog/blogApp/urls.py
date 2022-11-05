from django.urls import path
from.import views


app_name="blogApp"


urlpatterns = [
    path('home/',views.blog,name="blog"),
    path('add',views.blogAdd,name="Add"),
    path('read',views.blogRead,name="Read"),
    path("view/<post_id>", views.view_info, name="view_info"),
    path("view/<post_id>", views.delete, name="delete"),
    path("update/<post_id>",views.update, name="update")
    
  


]
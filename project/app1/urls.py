from django.urls import path
from . import views

app_name="app1"

urlpatterns=[

 path('home/', views.home, name="home"),
 path('addblog/', views.add_blog, name="add_blog"),
 path('Blog_D/<int:Blog_id>/',views.Blog_D , name="Blog_D"),
 path('update_blog/<int:Blog_id>/', views.update_Blog , name="update_Blog"),
 path('delete_Blog/<int:Blog_id>/',views.delete_Blog , name="delete_Blog"),
 

]


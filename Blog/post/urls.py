from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('list/', views.showPosts, name='list'),
    path('add/', views.addPost, name='add'),
    path('post/<post_id>/', views.postDetail, name='detail'),
    path('update/<post_id>/', views.updatePost, name='update'),
    path('delete/<post_id>/', views.deletePost, name='delete'),
    path('search/', views.searchPost, name='search')
]
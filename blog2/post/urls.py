from django.urls import path
from . import views



urlpatterns = [

    path('',views.post_add, name='new_post'),
    path('posts/',views.posts,name='posts'),
    path("posts/details/<post_id>/", views.post_d, name="posts_details"),
    path('posts/del/<post_id>/',views.del_post,name='dell_post')
    #path('post/id/','<post_id/>',)
]
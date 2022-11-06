

from django.shortcuts import render
from django.http import HttpRequest
from .models import blog
from datetime import date


def base(request: HttpRequest):
    return render(request, 'blog/home.html')


from django.shortcuts import render
from django.http import HttpRequest
from .models import Post
from datetime import date

# Create your views here.
def homePage(request: HttpRequest):
    return render(request, 'posts/home.html')

def showPosts(request: HttpRequest):
    posts = Post.objects.filter(is_published=True)
    context = {'posts':posts}
    return render(request, 'posts/read.html', context)

def addPost(request: HttpRequest):
    if request.method == 'POST':
        Post(title=request.POST['title'], content=request.POST['content'], is_published=request.POST['is_published'], publish_date=date.today()).save()
    return render(request, 'posts/add.html')
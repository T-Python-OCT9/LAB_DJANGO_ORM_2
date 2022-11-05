from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=2048)
    post_content = models.TextField()
    publish_date = models.DateTimeField()
    author_name = models.CharField(max_length=512)
    is_published =models.BooleanField()
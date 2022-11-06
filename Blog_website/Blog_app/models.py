from django.db import models

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=512)
    Content = models.TextField()
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField()

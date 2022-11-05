from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 2048)
    content =models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()





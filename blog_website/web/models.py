from django.db import models

# Create your models here.

class blogPost(models.Model,):
    
    title = models.CharField(max_length= 1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    is_published = models.BooleanField()



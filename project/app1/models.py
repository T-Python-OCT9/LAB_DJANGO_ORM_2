from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    is_published=models.BooleanField()
    publish_date = models.DateField()
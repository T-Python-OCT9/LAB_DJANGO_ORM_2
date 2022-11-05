from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    is_published=models.BooleanField()
    publish_date = models.DateField()

# Create your models here.

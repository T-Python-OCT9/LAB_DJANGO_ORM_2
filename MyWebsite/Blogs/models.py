from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    publish_date = models.DateTimeField()
    is_published = models.BooleanField()
from django.db import models

# Create your models here.
class Blog (models.Model):
    Title = models.CharField(max_length=2048)
    Content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()

class comment (models.Model):
    post = models.Forenkay(Blog)#ther is some themgh 
    #اوتو ناو هو الي يحدد الوقت اثناء الاضافه او التحديد 
    # بعد ما نخلص من المودل نسوي مقريشن و مقريت بعدين الفويوس 
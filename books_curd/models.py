from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100 , null=False)
    description = models.CharField(max_length=500 ,null=True)
    author = models.CharField(max_length=100)
    last_edit = models.DateTimeField(auto_now=True)
    image_url = models.URLField()
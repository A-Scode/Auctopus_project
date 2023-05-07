from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField()
    title = models.CharField(max_length=100 , null=False)
    description = models.CharField(max_length=500 ,null=True)
    
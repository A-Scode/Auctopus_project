from rest_framework import serializers
from .models import Book

class BookSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id',
                  'title',
                  'description',
                  'author',
                  'last_edit',
                  'image_url'
                  ]
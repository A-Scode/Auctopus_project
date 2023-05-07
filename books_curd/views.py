from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerailizer
from .models import Book

# Create your views here.
@api_view(['GET'])
def get_books_list(request):
    
    serialized_data = BookSerailizer(Book.objects.all() , many=True)
    
    return Response({'status':'success' , 'data':serialized_data.data})


    

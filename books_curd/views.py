from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerailizer
from .models import Book
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_books_list(request):
    
    serialized_data = BookSerailizer(Book.objects.all() , many=True)
    
    return Response({'status':'success' , 'data':serialized_data.data})


    
@api_view(['POST'])
def add_book(request):
    
    book = Book(
        title = request.data["title"],
        description = request.data["description"],
        author = request.data["author"],
        image_url = request.data["image_url"],
    )
    book.save()
    book.refresh_from_db()
    
    return Response({'status':'success' , 'data':{'book_id':book.book_id}})
    
@api_view(['POST'])
def delete_book(request):
    
    print(request.data)
    try:
    
        book = Book.objects.get(book_id = request.data['book_id'])
        book.delete()
        return Response({'status':'success'})
        
    except:
        return Response({'status':'error'} , status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def update_book(request):
    
    print(request.data)
    
    book = Book.objects.get(book_id= request.data['book_id'])
    book.title = request.data["title"]
    book.description = request.data["description"]
    book.author = request.data["author"]
    book.image_url = request.data["image_url"]
    
    book.save()
    
    
    return Response({'status':'success'})
    
    
    
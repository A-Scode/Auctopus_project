from django.urls import path
from .views import *


urlpatterns = [
    path('list/' , get_books_list , name="Books list" ),
    path('add/' , add_book , name="Books Add" ),
    path('delete/' , delete_book , name="Books Delete" ),
    path('edit/' , update_book , name="Books Update" ),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('list/' , get_books_list , name="Books list" ),
]
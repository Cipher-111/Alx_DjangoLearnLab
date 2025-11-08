from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-Based View: list all books
    path('books/', list_books, name='list_books'),

    # Class-Based View: show details of a specific library by primary key
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

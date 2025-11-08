from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Must import Library as required

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Must match the checker
    context_object_name = "library"  # Template expects 'library'

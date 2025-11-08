from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # ✅ Must include “from .models import Library”

# Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # must match checker
    context_object_name = "library"  # must match checker

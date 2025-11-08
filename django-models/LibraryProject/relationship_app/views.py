from django.shortcuts import render
from django.views.generic.detail import DetailView   # ✅ must be exactly like this
from .models import Library, Book  # ✅ must contain Library exactly like this

# Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

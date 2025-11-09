# relationship_app/views.py

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book, Library, UserProfile

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-based access helpers
def check_role(user, role_name):
    return hasattr(user, 'userprofile') and user.userprofile.role == role_name

@user_passes_test(lambda u: check_role(u, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: check_role(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: check_role(u, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Secured Book Views
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    pass  # Implement add logic here

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    pass  # Implement edit logic here

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    pass  # Implement delete logic here

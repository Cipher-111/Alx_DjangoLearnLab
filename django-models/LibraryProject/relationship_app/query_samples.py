import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Example: pick an author
author_name = "Author Name Here"  # Replace with an actual Author name in your DB
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# Example: pick a library by name
library_name = "Library Name Here"  # Replace with an actual Library name in your DB
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for that library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")

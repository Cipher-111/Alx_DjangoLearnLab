from bookshelf.models import Book
Book.objects.all().delete()
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

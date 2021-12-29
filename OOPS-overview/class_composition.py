#  Class composition is when a class contain other classes


class BookShelf:

    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("Harry Potter")
book2 = Book("Python 101")

print(book2)
print(book1)

shelf = BookShelf(book2, book1)
print(shelf)
print(shelf.books)


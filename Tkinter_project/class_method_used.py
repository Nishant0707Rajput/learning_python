class Book:

    TYPE = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<(Book: {self.name}, type: {self.book_type}, weight: {self.weight}g)>"

    @classmethod
    def hard_cover(cls, name, page_weight):
        return cls(name, cls.TYPE[0], page_weight + 100)

    @classmethod
    def paper_back(cls, name, page_weight):
        return cls(name, cls.TYPE[1], page_weight)


print(Book.TYPE)

# print()

an_instance = Book("Python101", "ANOTHER TYPE", 600)
print(an_instance)         # It is printing because of __repr__ method
print(Book)
book = Book.hard_cover("Harry Potter", 1500)
light = Book.paper_back("LOTR", 1800)


print(book)
print(light)

class TooManyPagesReadError(ValueError):
    pass

class Book:

    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.page_read} out of {self.page_count}>"
        )

    def read(self, pages):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(f"No. of pages in the Book is {self.page_count}."
                                        f"You tried to read {self.page_read + pages} pages")
        self.page_read += pages

        print(f"You have now read {self.page_read} out of {self.page_count}")


an_obj = Book("HarryPotter", 700)
# print(an_obj)
an_obj.read(500)
an_obj.read(100)
an_obj.read(400)
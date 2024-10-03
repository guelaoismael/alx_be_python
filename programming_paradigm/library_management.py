class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_check_out = False
    
    def check_out_book(self):
        self._is_check_out = True
    
    def return_book(self):
        self._is_check_out = False
    
    def is_available(self):
        return not self._is_check_out

class Library:
   
    def __init__(self) -> None:
        self._books = []

    def add_book(self, book):

        if isinstance(book, Book):
            self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out_book()
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title :
                book.return_book()
    
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
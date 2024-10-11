class Book:
    def __init__(self, title:str, author:str):
        self.title =  title
        self.author =  author
   
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author)
        #Additional attribute initialization
        self.file_size = file_size
    
    def __str__(self):
        return (f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")

class PrintBook(Book):
   def __init__(self, title:str, author:str, page_count:int):
       super().__init__(title, author)
       #Additional attribute initialization
       self.page_count = page_count

   def __str__(self):
      return (f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}")


class Library:

    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("This type is not a book, only Book, Ebook or PrintBook can be added.")
        else:
            self.books.append(book)
            # print(f"{book} added")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(f"{book}")
        
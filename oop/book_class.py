class Book:
    """_____Creating a Book class_____"""
    
   # Initializer method that assigns values to the attributes title, author, and year of an object.
    def __init__(self, title : str, author : str, year : int):
       
        self.title = title
        self.author = author
        self.year = year
    
    # Magic method returns a formatted string representing the title, author, and publication year of a book
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    # Magic method returns a string representation of a Book object with its title, author, and year.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
   
    # The above function is a Python method that prints a message when an object is deleted. 
    def __del__(self):
        print(f"Deleting {self.title}")
    
   
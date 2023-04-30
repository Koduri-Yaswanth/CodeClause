class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = "Available"
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_book_id(self):
        return self.book_id
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
    def search_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None
    
    def checkout_book(self, book):
        if book.get_status() == "Available":
            book.set_status("Checked Out")
            return True
        else:
            return False
    
    def return_book(self, book):
        book.set_status("Available")
        return True
    
    def display_books(self):
        for book in self.books:
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("Book ID:", book.get_book_id())
            print("Status:", book.get_status())
            print()

# create a library object
my_library = Library("My Library")

# Adding books
book1 = Book("It Ends with Us", "Collen Hoover", 1)
book2 = Book("One Arranged Murder", "Chetan Bhagat", 2)
book3 = Book("Harry Potter", "J.K.Rowling", 3)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# display all the books in the library
print("All books in the library:")
my_library.display_books()

# search for a book by title
book = my_library.search_book("Harry Potter")
if book:
    print("Book found!")
    print("Title:", book.get_title())
    print("Author:", book.get_author())
    print("Book ID:", book.get_book_id())
    print("Status:", book.get_status())
else:
    print("Book not found.")
    

# checkout a book
if my_library.checkout_book(book2):
    print("Book checked out successfully.")
else:
    print("Book is not available for checkout.")

# display all the books in the library
print("All books in the library:")
my_library.display_books()


# return a book
if my_library.return_book(book2):
    print("Book returned successfully.")
else:
    print("Book is not checked out.")

# display all the books in the library
print("All books in the library:")
my_library.display_books()
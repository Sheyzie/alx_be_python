# base class
class Book:

  def __init__(self, title: str, author: str):
    self.title = title
    self.author = author

class EBook(Book):

  def __init__(self, title: str, author: str, file_size: int):
    self.file_size = file_size
    super().__init__(title, author)

class PrintBook(Book):

  def __init__(self, title: str, author: str, page_count: int):
    self.page_count = page_count
    super().__init__(title, author)

class Library:

  def __init__(self):
    self.books = []
  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    for book in self.books:
      if hasattr(book, 'file_size'):
        print(f'{book.__class__.__name__}: {book.title} by {book.author}, File Size: {book.file_size}')
      elif hasattr(book, 'page_count'):
        print(f'{book.__class__.__name__}: {book.title} by {book.author}, Page Count: {book.page_count}')
      else:
        print(f'{book.__class__.__name__}: {book.title} by {book.author}')

  def __str__(self):
    return f'{self.books}'
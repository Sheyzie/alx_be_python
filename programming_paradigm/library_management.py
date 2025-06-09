
class Book:
  title = ''
  author = ''
  _is_checked_out = False

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def check_out_book(self):
    if self._is_checked_out == True:
      return f'Sorry, the book title {self.title} is not available'
    else:
      self._is_checked_out = True
      return f'The book title {self.title} is checked out'
    
  def  return_book(self, title):
    if self._is_checked_out == False:
      return f'Sorry, the book title {self.title} is already available in Library'
    else:
      self._is_checked_out = False
      return f'The book title {self.title} is returned to Library'

class Library:

  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)

  def check_out_book(self, title):
    book_found = False
    for book in self._books:
      if book.title == title:
        result = book.check_out_book()
        book_found = True

    if book_found:
      print(result)
    else:
      print(f'Sorry, the book title {title} not found')    
  
  def return_book(self, title):
    book_found = False
    for book in self._books:
      if book.title == title:
        result = book.return_book(title)
        book_found = True

    if book_found:
      print(result)
    else:
      print(f'Sorry, the book title {title} not found')  

  def list_available_books(self):
    for book in self._books:
      print(f'{book.title} by {book.author}')  

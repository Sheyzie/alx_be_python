#!/usr/bin/env python

class Book:

  def __init__(self, title: str, author: str, year: int):
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    return f'{self.title} by {self.author}, published in {self.year}'
  
  def __repr__(self):
    return f"{self.__class__.__name__}('{self.title}', '{self.author}', {self.year})"
  
  def __del__(self):
    print(f'Deleting {self.title}')
# Book related functions
from dj import development_tools  as log
import os
import codecs 
from markov_functions.models import Book


def load_book(bookID=False):
  try:
    
    log.g_log_exception(bookID)
    book = Book.objects.get(pk=bookID) #bookID)

    #log.g_log_exception("Book: " + book)
    contents = book.file.read().decode()
    return str(contents)
  except:
    log.g_log_exception(log.PrintException())
    return "Failed"

def load_active_books(listOfBooks):
  """ Takes a list of books by ID and loads them into a text string """
  text = ""
  for book in listOfBooks:
    text += load_book(book)
  return text
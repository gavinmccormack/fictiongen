# Book related functions
from dj import development_tools  as log
import os
import codecs 
from markov_functions.models import Book


def load_book(bookID=False):
  try:
    book = Book.objects.get(pk=1) #bookID)
    contents = book.file.read().encode('utf-8')
    return str(contents)
  except:
    log.g_log_exception(log.PrintException())
    return "Failed"

def load_active_books(listOfBooks):
  """ Takes a list of books by ID and loads them into a text string """
  text = ""
  for book in listOfBooks:
    text += load_book()
  return text
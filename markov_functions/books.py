# Book related functions
from dj import development_tools  as log
import os
import codecs 

def load_book(filename="ulysses.txt"):
  try:
    path = os.path.join(os.path.dirname(__file__), 'books', filename)
    with codecs.open(path, "r", encoding='utf-8') as file:    # Codec module to avoid ascii encode/decode errors 
      bookText = file.read()
    bookText = "".join(bookText).strip().encode()
    return bookText
  except:
    log.g_log_exception(log.PrintException())

def load_active_books(listOfBooks):
  """ Takes a list of books by ID and loads them into a text string """
  text = ""
  for book in listOfBooks:
    text += load_book()
  return text
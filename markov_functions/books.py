# Book related functions
from dj import development_tools  as log
import os
import codecs 
from markov_functions.models import Book
import markovify

## These should maybe be part of models.py
def build_model(text, conf_state_size, posEnabled=False):
    try:
      posEnabled = False
      if posEnabled:
        log.g_log_exception("Type: NLTK")
        return (nltk.POSifiedText(text, state_size=conf_state_size))
      else:
        log.g_log_exception("Type: Simple")
        return (markovify.Text(text, state_size=conf_state_size))
    except:
      log.g_log_exception(log.PrintException())
      return "Failed"

def get_book_model(bookID, stateSize, posEnabled):
  try:
    book = Book.objects.get(pk=bookID) 
    contents = book.file.read().decode('utf-8','ignore')
    model = build_model(contents, int(stateSize), posEnabled=posEnabled)
    return model
  except:
    log.g_log_exception(log.PrintException())
    return "Failed"

def load_active_books(active_books, stateSize, posEnabled):
  """ Takes a list of books by ID and loads them into a text string """
  try:
    text = ""
    combined_models = build_model("", stateSize, posEnabled) # Initialise a blank text object to combine with
    print(active_books)
    for book,weight in active_books.items():
      book_model = get_book_model(int(book), stateSize, posEnabled)
      print(combined_models)
      combined_models = markovify.combine([combined_models, book_model],[ 1 , int(weight) ]) # Combine total model with current loop model with it's prescribed weight.
    return combined_models
  except:
    log.g_log_exception(log.PrintException())
    return "Failed"

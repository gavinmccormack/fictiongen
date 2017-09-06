# encoding=utf8  
import markovify
import sys
import os
from dj import development_tools  as log
from markov_functions.text_processors import mk_nltk #, mk_textacy
from .books import load_active_books

##############################################################################
###### Markov FUnctions


class fictionObject(object):
  """ This is a wrapper for the markovText method with features for our application """
  def __init__(self, books={}, stateSize=2):
    print("Init!")
    self.books =  books
    self.stateSize = int(stateSize)
    print("Init finished")


  def get_text(self, lines=30, posEnabled=0, line_breaks=3):
    """ Method needs refactored particularly in light of proper book models """
    log.g_log_exception("Beginning markovification")
    try: 
      model = load_active_books(self.books, self.stateSize, posEnabled) 
      output = self.get_mk_sentences(model, lines ,line_breaks)
      return output
    except:
      log.g_log_exception(log.PrintException())
      return False

  def get_mk_sentences(self, textModel, numberOfLines, line_breaks):
    output = ""
    for i in range(numberOfLines):
        sentence = str(textModel.make_sentence()) + " " # Spaces after full stop
        if sentence != "None ":
          if i % line_breaks == 0:          # Add in line breaks every so often, just for a bit more of a normal appearance, add this to front end
            output = output + "<br />"
          output = output + sentence 
    return output 



def save_model(model):
  """ Takes a markovify text model and dumps it as JSON to a file """
  save_model_path = "Should look into using Django storage functions."
  with open("Example_Model_Path.txt",'w') as f:
      json.dump(model.to_json(), f)

def get_saved_model(bookID, testingFilePath):
  with open(testingFilePath, 'rb') as f:
    f.read()



def markovify_sentence(text_model): # Extended the markov method to fail silently
  sentence = text_model.make_sentence()
  if not(sentence is None):
    return sentence.unicode()

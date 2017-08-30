# encoding=utf8  
import markovify
import sys
import os
from dj import development_tools  as log
from markov_functions import nltk
from .books import load_book

##############################################################################
###### Markov FUnctions

def build_model(text, conf_state_size, posEnabled=False):
  posEnabled = False
  if posEnabled:
    log.g_log_exception("Type: NLTK")
    return (nltk.POSifiedText(text, state_size=conf_state_size))
  else:
    log.g_log_exception("Type: Simple")
    return (markovify.Text(text, state_size=conf_state_size))

def save_model(model):
  """ Takes a markovify text model and dumps it as JSON to a file """
  save_model_path = "Should look into using Django storage functions."
  with open("Example_Model_Path.txt",'w') as f:
      json.dump(model.to_json(), f)

def get_saved_model(bookID, testingFilePath):
  with open(testingFilePath, 'rb') as f:
    f.read()

def markovify_text(text="", lines=30, bookIDs=[], posEnabled=0, stateSize=2, line_breaks=3 ):
  """ Method needs refactored particularly in light of proper book models """
  log.g_log_exception("Beginning markovification")
  # an array of ID's for books, but at the moment .txt refs
  # The verbose method of creating the dict is used so that we can have integer keys.
  books = dict([("ulysses.txt", 1)]) 
  try: 
    text = load_book(1) #bookIDs)
    log.g_log_exception(text)
    mtext = build_model(text, stateSize, posEnabled)
    output = ""
    for i in range(int(lines)):
      sentence = str(mtext.make_sentence()) + " " # Spaces after full stop
      if sentence != "None ":
        if i % line_breaks == 0:          # Add in line breaks every so often, just for a bit more of a normal appearance, add this to front end
          output = output + "<br />"
        output = output + sentence 
    return output
  except:
    log.g_log_exception("Generating text failed for the following reason:")
    log.g_log_exception(log.PrintException())
    return False


def markovify_sentence(text_model): # Extended the markov method to fail silently
  sentence = text_model.make_sentence()
  if not(sentence is None):
    return sentence.unicode()

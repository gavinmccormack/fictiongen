# encoding=utf8  
import markovify
import sys
import os
from dj import development_tools  as log
from markov_functions import nltk

##############################################################################
###### Markov FUnctions

def build_model(text, conf_state_size, posEnabled=False):
  if posEnabled:
    log.g_log_exception("We used fancy piece of shit text")
    return (POSifiedText(text, state_size=conf_state_size))
  else:
    log.g_log_exception("We used good old simple markov chain")
    return (markovify.Text(text, state_size=conf_state_size))


def markovify_text(text, lines, books, posEnabled, conf_state_size=2, line_breaks=3 ):
  """ Method needs refactored particularly in light of proper book models """
  log.g_log_exception("Begin markovification")
  books = ["ulysses.txt"] # an array of ID's for books, but at the moment .txt refs
  try: 
    text = text + load_book()
    text = text + load_book( "megarotic.txt" )
    text = text.decode('utf-8')
    mtext = build_model(text,conf_state_size, int(posEnabled))
    output = ""
    for i in range(int(lines)):
      sentence = str(mtext.make_sentence()) + " " # Spaces after full stop
      if sentence != "None ":
        if i % 5 == 0:          # Add in line breaks every so often, just for a bit more of a normal appearance, add this to front end
          output = output + "<br />"
        output = output + sentence 
    #output = changePronouns(output)
    return output
  except:
    log.g_log_exception("Generating text failed for the following reason:")
    log.g_log_exception(log.PrintException())
    return False


def markovify_sentence(text_model): # Extended the markov method to fail silently
  sentence = text_model.make_sentence()
  if not(sentence is None):
    return sentence.unicode()


#############################################################################
###### Text Pre-Processors
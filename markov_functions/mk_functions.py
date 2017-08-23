# encoding=utf8  
import markovify
import time
import linecache
import sys
import os
import re
import nltk
import datetime
import random
import importlib
import codecs
from dj import development_tools  as log

importlib.reload(sys)  
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data')) ## Add NLTK grammars & tagging

## Experimental and humourin' modules

def tag_check(tag):
  """ Replace certain types of words with bizarre food alternatives. Prototype; needs refactoring/fixing """
  gross_words_list = ['meat','ham'] #,'salami','pork','jelly','cake']
  gross_words_list_p = ["meat's"] #,"ham's","salami's","pork's","jelly's","cake's"]
  singular = ['NN'] # NNP, NN 
  plural =  ['NNS'] # bacons 'NNPS','NNS''
  ownership = ['PRP$','POS'] # bacon's
  if tag[1] in singular:
    return random.choice(gross_words_list) + "::"+tag[1]
  if tag[1] in plural:
    return random.choice(gross_words_list_p) + "::"+tag[1]
  else:
    log.g_log_exception(tag,"NLTK_words.txt")
    return "::".join(tag)

  # NNP, NN

  # NNPS, NNS (plural)

  # PRP$ , POS, Belongs to 's



## override markovify text method with POS natural language
class POSifiedText(markovify.Text):
  """ Extend markovify.text method to use POS """
  def word_split(self, sentence):
    try:
      words = re.split(self.word_split_pattern, sentence)
      words_cache = []
      for tag in nltk.pos_tag(words):
          try:
            words_cache.append( tag_check(tag) )
          except Exception as e:
            log.g_log_exception("POSifiedText Problem" ,"NLTK_words.txt",exception=True)

      words = words_cache
      return words
    except Exception as e:
      log.g_log_exception("Test P Except", exception=True)
      return words

  def word_join(self, words):
    sentence = " ".join(word.split("::")[0] for word in words)
    return sentence




#############################################################################
###### Proper code

def build_model(text, conf_state_size, posEnabled=False):
  if posEnabled:
    log.g_log_exception("We used fancy piece of shit text")
    return (POSifiedText(text, state_size=conf_state_size))
  else:
    log.g_log_exception("We used good old simple markov chain")
    return (markovify.Text(text, state_size=conf_state_size))

def load_book(filesize, filename="ulysses.txt"):
  try:
    log.g_log_exception("Begin book load")
    path = os.path.join(os.path.dirname(__file__), 'books', filename)
    log.g_log_exception("Booksize: " + str(filesize) + " / Filename: " + filename)
    with codecs.open(path, "r", encoding='utf-8') as file:    # Codec module to avoid ascii encode/decode errors 
      bookText = [next(file) for x in range(filesize)]
    bookText = " ".join(bookText).strip()
    bookText = bookText.encode('utf8')
    log.g_log_exception("Book load ended")
    return bookText
  except:
    log.g_log_exception("Book load failed for the following reason:")
    log.g_log_exception(log.PrintException())

def markovify_text(text, lines, ulysses, erotic, posEnabled, conf_state_size=2 ):
  log.g_log_exception("Begin markovification")
  try: 
    text = text + load_book( int(ulysses) )
    text = text + load_book( int(erotic) , "megarotic.txt")
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
    log.g_log_exception("End markovification")
    return output
  except:
    log.g_log_exception("Generating text failed for the following reason:")
    log.g_log_exception(log.PrintException())
    return "Failed to generate any text : ("


def markovify_sentence(text_model): # Extended the markov method to fail silently
  sentence = text_model.make_sentence()
  if not(sentence is None):
    return sentence.unicode()
  return "[~Could not find a match~]" ## Not sure what this is doing here anymore - too many revisions.


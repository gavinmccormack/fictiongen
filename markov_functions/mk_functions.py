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

importlib.reload(sys)  
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

MARKOV_LOGGING = False # Hook this up to logging function 

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)



def g_log_exception(err, filename="general_log.txt", exception=False):
  if MARKOV_LOGGING:
    errorFile = open(os.path.join(os.path.dirname(__file__), 'errors', filename), "a")
    startTime = time.time()
    startTime = datetime.datetime.fromtimestamp(startTime) # check 
    errorFile.write("Time: " + str(startTime) + "  ")
    errorFile.write(str(err))
    if exception:
      errorFile.write("\n" + PrintException())
    errorFile.write("\n")
    errorFile.close()


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
    g_log_exception(tag,"NLTK_words.txt")
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
            g_log_exception("POSifiedText Problem" ,"NLTK_words.txt",exception=True)

      words = words_cache
      return words
    except Exception as e:
      g_log_exception("Test P Except", exception=True)
      return words

  def word_join(self, words):
    sentence = " ".join(word.split("::")[0] for word in words)
    return sentence




#############################################################################
###### Proper code

def build_model(text, conf_state_size, posEnabled=False):
  if posEnabled:
    g_log_exception("We used fancy piece of shit text")
    return (POSifiedText(text, state_size=conf_state_size))
  else:
    g_log_exception("We used good old simple markov chain")
    return (markovify.Text(text, state_size=conf_state_size))

def load_book(filesize, filename="ulysses.txt"):
  try:
    g_log_exception("Begin book load")
    path = os.path.join(os.path.dirname(__file__), 'books', filename)
    g_log_exception("Booksize: " + str(filesize) + " / Filename: " + filename)
    with codecs.open(path, "r", encoding='utf-8') as file:    # Codec module to avoid ascii encode/decode errors 
      bookText = [next(file) for x in range(filesize)]
    bookText = " ".join(bookText).strip()
    bookText = bookText.encode('utf8')
    g_log_exception("Book load ended")
    return bookText
  except:
    g_log_exception("Book load failed for the following reason:")
    g_log_exception(PrintException())

def markovify_text(text, lines, ulysses, erotic, posEnabled, conf_state_size=2 ):
  g_log_exception("Begin markovification")
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
    g_log_exception("End markovification")
    return output
  except:
    g_log_exception("Generating text failed for the following reason:")
    g_log_exception(PrintException())
    return "Failed to generate any text : ("


def markovify_sentence(text_model): # Extended the markov method to fail silently
  sentence = text_model.make_sentence()
  if not(sentence is None):
    return sentence.unicode()
  return "[~Could not find a match~]" ## Not sure what this is doing here anymore - too many revisions.






## To do
### - Clean up code. It's shit
### Redo sentences if they provide a None result
### Parse ASCII characters awaaay! awaay with them!
def markovify_whatsapp(text,lines):
  poname = 'Bob: '
  ptname = 'Sally: '
  pot = "1:"
  ptt = "2:"
  processedText = ""
  file_i = 0
  try:
    for line in text.splitlines():
      line = line.encode('utf-8')
      if not line:
        i = line.find(':')
        line = line[i+5:]
        if (line.find('Hannah') > 0):
          pot = pot + (line.split(':')[1]) + '\n'
        elif (line.find('Wisearse') > 0):
          ptt = ptt + (line.split(':')[1]) + '\n'
        if i == -1:
          pass
  except Exception as e:
    return "fuck" + str(e)
  try:
    pot = markovify.NewlineText(pot, state_size=1)
    ptt = markovify.NewlineText(ptt, state_size=1)
    for n in range(int(lines)):
      processedText = processedText + "<br/>" + poname  + markovify_sentence(pot)
      processedText = processedText + "<br/>" + ptname  + markovify_sentence(ptt)
  except Exception as e:
    return "Second: " + str(e)
  return processedText

def test():
  return "Y"
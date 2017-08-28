
from dj import development_tools  as log
import random
import nltk
import importlib
import sys
import os
import markovify
import re



importlib.reload(sys)  
nltk.data.path.append(os.path.join(os.path.dirname(__file__), 'nltk_data'))

def tag_check(tag):
  """ Replace certain types of words with bizarre food alternatives. 
  I realise that the NLTK features more or less boil down to this inanity at the moment
  Prototype; needs refactoring/fixing """
  gross_words_list = ['meat','ham'] #,'salami','pork','jelly','cake']
  gross_words_list_p = ["meat's"] #,"ham's","salami's","pork's","jelly's","cake's"]
  singular = ['NNP'] # NNP, NN 
  plural =  ['NNPS'] # bacons 'NNPS','NNS''
  #ownership = ['PRP$','POS'] # bacon's
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
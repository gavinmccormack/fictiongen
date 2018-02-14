
from core import development_tools  as log
import random
import nltk
import importlib
import sys
import os
import markovify
import re
from . import fickgen_splitters as f_split



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
    return "::".join(tag)




## override markovify text method with POS natural language
class POSifiedText(markovify.Text):
  """ Extend markovify.text method to use POS """

  def word_split(self, sentence):
    try:
      words = re.split(self.word_split_pattern, sentence)
      words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
      return words

      ## The below is the "tag check" method.
      # This is next on the hit list of code to be improved. Tis a mess !
      words_cache = []
      for tag in nltk.pos_tag(words):
          try:
            words_cache.append( tag_check(tag) )
          except Exception as e:
            log.exception(err="POSifiedText Problem", filename="nltk_errors.log")
      words = words_cache
      return words
    except Exception as e:
      log.exception(err="TPOSifiedText Problem", filename="nltk_errors.log")
      return words

  def word_join(self, words):
    sentence = " ".join(word.split("::")[0] for word in words)
    return sentence

  def sentence_split(self,text):
    """ Not in used yet: Override the default splitting and also include commas """
    return self.split_into_sentences(text)

  def split_into_sentences(self, text):
    return f_split.split_into_sentences(text)


def get_names(filename):
    with open(filename,'r',encoding='utf-8') as name_source:
        names = [name.strip() for name in name_source]
        return names
        
def run_regex_union():
    """ Matches names in names list and replaces with "Sally". """
    nameList = get_names("nltk_data/male_names.txt")
    def replace_names(match_object):
      name = match_object.group(0)
      if name in nameList:
          return "Sally"
      else:
          return name
    with open(file,'r', encoding='utf-8') as f:
        output = f.read()
        output = re.sub('\w+', replace_names, output)

    with open("fin-" +file,'w',encoding='utf-8') as f:
        f.write(output)
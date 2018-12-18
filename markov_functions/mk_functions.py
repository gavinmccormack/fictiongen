# encoding=utf8  
import markovify
import sys
import os
from core import development_tools  as log
from markov_functions.text_processors import mk_nltk #, mk_textacy
from .books import load_active_books

##############################################################################
###### Markov Functions


class fictionObject(object):
  """ This is the parent class for text generation. """
  def __init__(self, request_data):
    """ The JSON format comes in as string, so we'll need to do some typecasting here """
    self.config = request_data
    self.config['pos_enabled'] = int(self.config['pos_enabled'])
    self.config['state_size'] = int(self.config['state_size'])
    self.config['number_of_sentences'] = int(self.config['number_of_sentences'])
    self.config['size_of_paragraphs'] = int(self.config['size_of_paragraphs'])

  def get_text(self, config):
    """ Returns generated text based on the active books """
    try: 
      model = load_active_books(self.config) 
      generated_text = self.get_mk_sentences(model, self.config)   
      return generated_text
    except:
      log.exception()
      return False

  def get_mk_sentences(self, model, config):
    output = ""
    for i in range(self.config['number_of_sentences']):
        sentence = str(model.make_sentence()) + " " # Spaces after full stop
        if sentence != "None ":
          if i % self.config['size_of_paragraphs'] == 0: 
            output = output + "<br />" # Add line breaks as per paragraph size
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

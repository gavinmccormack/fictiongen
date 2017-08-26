from django.test import TestCase, Client
import os
# Test specific 
from markov_functions import books, mk_functions
import json

#################################
# Markov Function unit tests
#################################
# Tests must start with test.
# Basic Essential functionality:


test_resources_directory = os.path.dirname(os.path.realpath(__file__))

class test_books(TestCase):
	def setUp(self):
		# Database setup for tests
		self.loaded_text = books.load_book(15,"ulysses.txt")[0:50]

	def test_load_book_simple(self):
		""" Test case only covers first 50 characters. Newlines and other encoding errors untested """
		test_file = os.path.join(test_resources_directory,'resources','test_book.txt')
		with open(test_file,'r',encoding='utf8') as f:
			test_text = f.read()
			test_text = "".join(test_text).strip()[0:50]

		self.assertEqual(self.loaded_text,test_text)

	def test_book_encoding(self):
		try:
		    self.loaded_text.encode('utf-8')
		except UnicodeError:
		    self.fail("Book input is not utf-8") 

	def test_load_active_books(self):
		## Test the load_active_books function when operational
		pass

class test_internal_mk_functions(TestCase):
	def setUp(self):
		self.loaded_text_5_chars = books.load_book(15,"ulysses.txt")[0:5]
		self.loaded_text_50_chars = books.load_book(15,"ulysses.txt")[0:50]
		self.loaded_text_500_chars = books.load_book(15,"ulysses.txt")[0:500]
		self.model = mk_functions.build_model(self.loaded_text_50_chars, 1)
		self.valid_model_path = os.path.join(test_resources_directory,'resources','model_json_1.json')

	def save_build_model(self):
		""" Not a test, but this will save a generated model to use to validate the output """
		with open(self.valid_model_path,'w') as f:
			json.dump(self.model.to_json(), f)

	def test_build_model(self):
		with open(self.valid_model_path ,'r') as f:
			valid_model = json.loads(f.read())
			tested_model = self.model.to_json()
			tested_model = json.loads(tested_model)
			self.assertEqual(self.model.to_json(), valid_model) # Currently failing, need to investigate better ways of validating data objects

class test_mk_functions_request_views(TestCase):
	def setUp(self):
		self.cli = Client()

	def test_ma_process(self):
		request = self.cli.post('/mk/process/', {"marktext" : "I am the input text", "lines" : 5, "ulysses" : 500,
										"erotic" : 500, "stateSize" : 1, "grammar" : False })
		self.assertEqual(request.status_code, 200)
		print(request.content)
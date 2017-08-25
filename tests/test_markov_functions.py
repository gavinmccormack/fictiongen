from django.test import TestCase
import os
# Test specific 
from markov_functions import *

#################################
# Markov Function unit tests
#################################
# Tests must start with test.
# Basic Essential functionality:

class test_basic_text(TestCase):
	def setUp(self):
		# load in files
		pass

	def test_load_book_simple(self):
		""" Test case only covers first 50 characters. Newlines and other encoding errors untested """
		test_resources_directory = os.path.dirname(os.path.realpath(__file__))
		test_file = os.path.join(test_resources_directory,'resources','test_book.txt')
		with open(test_file,'r',encoding='utf8') as f:
			test_text = f.read()
			test_text = "".join(test_text).strip()[0:50]
		loaded_text = mk_functions.load_book(15,"ulysses.txt")[0:50]
		self.assertEqual(loaded_text,test_text)
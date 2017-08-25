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
		
	def test_load_book_short(self):
		""" Filesizes to be removed from book load functions """
		#text = mk_functions.load_book(15,"megarotic.txt")
		#
		# self.assertEqual(text, "I am the middle" )
		pass

	def test_load_book_long(self):
		test_resources_directory = os.path.dirname(os.path.realpath(__file__))
		test_file = os.path.join(test_resources_directory,'resources','test_book.txt')
		with open(test_file,'r',encoding='utf8') as f:
			test_text = f.read()
			test_text = "".join(test_text).strip()
		loaded_text = mk_functions.load_book(15,"ulysses.txt")
		self.assertEqual(loaded_text,test_text)
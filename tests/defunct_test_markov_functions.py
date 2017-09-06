from django.test import TestCase, Client
import os
# Test specific 
from markov_functions import books, mk_functions
from markov_functions.models import Book
import json
from django.contrib.auth.models import User
from django.core.files import File
import os
#################################
# Markov Function unit tests
#################################
# Tests must start with test.
# Basic Essential functionality:

test_resources_directory = os.path.dirname(os.path.realpath(__file__))

# Database initialization
db_run_once = False
def init_test_database():
	global db_run_once
	if db_run_once:
		pass
	testUser = User.objects.create(username="testuser", password="test",is_superuser=True)
	filePath = os.path.join(os.path.dirname(__file__), "resources", "test_book.txt")

	print("Loading a test book file...")
	print(filePath)
	testFileContents = ""
	with open(filePath,'r',encoding='utf-8') as f:
		testFileContents = f

		# Init books
		print("Creating a book object for testing...")
		testBook = Book.objects.create(name="Book",user=testUser)
		testBook.file.save("Test Book", File(testFileContents))
		testBook.save()
		print("Book ID: " + str(testBook.id))


	print("Testing retrieval of book object...")
	book = Book.objects.get(pk=1)
	print(book)
	db_run_once = True # Bit of a weird way of doing it.
	print("Database Init finished")

class test_books(TestCase):
	def setUp(self):
		# Database setup for tests
		self.loaded_text = books.load_book(1)
		init_test_database()

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
		self.loaded_text_5_chars = books.load_active_books({32,100})[0:5]
		self.model = mk_functions.build_model(self.loaded_text_5_chars, 1)
		self.valid_model_path = os.path.join(test_resources_directory,'resources','model_json_1.json')
		init_test_database()

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
		self.request = self.cli.post('/mk/process/', 
			 {"lines" : 5, 
			 "stateSize" : 1,
			 "posEnabled" : 1,
			 "bookid" : 1 # should be list, and then dict with weights.
			})
		init_test_database()
		

	def test_ma_process_response(self):
		self.assertEqual(self.request.status_code, 200)

	def test_ma_process_content(self):
		""" The markov generation pipe has failed """
		# Returning false as a byte code is odd. So it'd be better if the
		# status code changed.
		print("Output of content (or Error):\n")
		print(str(self.request.content) + "\n")
		self.assertNotEqual(self.request.content, b"False")

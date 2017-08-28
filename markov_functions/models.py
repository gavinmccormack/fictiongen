# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from . import mk_functions
from django.core.files import File
from django.core.files.base import ContentFile
from dj.settings import MEDIA_ROOT

# from djutils.decorators import async     # Python 3 errors. Find alternative or fix lib

def save_book_models(book, state_range=[2,5]):
  """ Takes a file object, creates several models and stores them alongside the original """
  generated_model = mk_functions.build_model(book.read().decode('UTF-8'), 2)# add in loop for # of ranges

  filename = book.path + "_model_2.txt"
  book = File(book)
  with open(filename, 'w') as output_file:
    output_file.write(generated_model.to_json())
    output_file.write(book.read().decode('UTF-8'))
    output_file.write("End")
  return True

def decode_file(file):
  pass

def get_book_directory_path(instance, filename):
  # File directory for books; only used for local access.
  # To do for portability; implement constant
  return 'user/{0}/{1}'.format(instance.user.id, filename)

class Book(models.Model):
  name = models.CharField(max_length=30)
  file = models.FileField(upload_to=get_book_directory_path)
  user = models.ForeignKey(User, unique=False)
  created     = models.DateTimeField(editable=False)
  modified    = models.DateTimeField()

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created = timezone.now()
    self.modified = timezone.now()

    save_book_models(self.file)     # would be nice to decode the books on upload so it's not a pita
    return super(Book, self).save(*args, **kwargs)

  def __str__(self):
    return 'Book: ' + self.name

  class Meta:
    verbose_name = 'Book'
    verbose_name_plural = 'Site Books'

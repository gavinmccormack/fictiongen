# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markov_functions.books import save_book_models
from django.core.files import File
from django.core.files.base import ContentFile
from core.settings import MEDIA_ROOT

def get_book_directory_path(instance, filename):
  # File directory for books; only used for local access.
  # To do for portability; implement constant
  return 'user/{0}/{1}'.format(instance.user.id, filename)

class Book(models.Model):
  name = models.CharField(max_length=80,blank=True)
  file = models.FileField(upload_to=get_book_directory_path,blank=True)
  model = models.FileField(upload_to=get_book_directory_path,blank=True) # Model is saved on first use
  user = models.ForeignKey(User, unique=False,blank=True, on_delete=models.CASCADE,)
  author = models.CharField(max_length=60,blank=True)
  created     = models.DateTimeField(editable=False,blank=True)
  modified    = models.DateTimeField(blank=True)
  lines       = models.IntegerField(blank=True)
  sentences      = models.IntegerField(blank=True)

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.created = timezone.now()
    self.modified = timezone.now()

    fileContents = self.file.read().decode('utf-8','ignore')
    self.lines = len(fileContents.split(' '))
    self.sentences = len(fileContents.split('.'))
    return super(Book, self).save(*args, **kwargs)

  def __str__(self):
    return 'Book: ' + self.name

  class Meta:
    verbose_name = 'Book'
    verbose_name_plural = 'Site Books'
 
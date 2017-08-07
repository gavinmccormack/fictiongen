from django.core.urlresolvers import reverse
from django.test import TestCase 
from markov_functions import mk_functions as mk

@tag ('markov', 'core')
class markovTest(TestCase):
  def test_large_corpus(self):
    self.response = self.client.get(reverse('process'))
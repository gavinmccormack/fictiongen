from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt 
import markov_functions.mk_functions as ma
from markov_functions.models import Book

def index(request):
    books_query = Book.objects.all()
    context = {'books_query': books_query}
    return render_to_response('index.html', context)

def homepage(request):
    context = {}
    context['books'] = Book.objects.all()
    return render_to_response('homepage.html', context)



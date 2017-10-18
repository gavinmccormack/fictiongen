from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt ## insecure - fix
# Create your views here.
import markov_functions.mk_functions as ma # Test
from markov_functions.models import Book

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)



def index(request):
    books_query = Book.objects.all()
    context = {'books_query': books_query}
    return render_to_response('index.html', context)

def homepage(request):
    context = {}
    context['books'] = Book.objects.all()
    return render_to_response('homepage.html', context)



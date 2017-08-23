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
	context = {}
	return render_to_response('index.html', context)

def homepage(request):
	context = {}
	context['books'] = Book.objects.all()
	return render_to_response('homepage.html', context)



# Post call to whatsapp text
@csrf_exempt
def ma_process(request):
	""" Send text to algorithm and return response """
	context_instance=RequestContext(request)
	if request.method == 'POST':
		try:
			markovedText = ma.markovify_text(
				request.POST['marktext'].encode('utf-8'),
				request.POST['lines'],  
				request.POST['ulysses'], 
				request.POST['erotic'], 
				request.POST['grammar'], 
				int(request.POST['stateSize']), )
			return HttpResponse(markovedText.encode('utf-8'))
		except Exception as e:
			return HttpResponse(PrintException())
	return HttpResponse("Request was not sent as POST request.")

@csrf_exempt
def ma_process_whatsapp(request):
	""" Send whatsapp text to algorithm and return response """
	context_instance=RequestContext(request)
	if request.method == 'POST':
		try:
			markovedText = ma.markovify_whatsapp(request.POST['whattext'].encode('utf-8'), request.POST['lines'])
			return HttpResponse(markovedText)
		except Exception as e:
			return HttpResponse("I'm sorry, I've failed you and there was an error :" + str(e) )
	return HttpResponse("A query was not correctly sent to the chatbot")


@csrf_exempt
def steal_text(request):
	response = steal_from_url(request.POST['url'])
	return HttpResponse(response)

@csrf_exempt
def compile_scripts(request):
	import os
	result = os.system('python -m compileall ' + os.path.dirname(__file__)) # Not working atm, likely apache user permissions 
	return HttpResponse("Scripts compiled: " + str(result))

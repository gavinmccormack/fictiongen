from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt ## Temporary
#from web_functions import steal_from_url
from django.template import RequestContext
import markov_functions.mk_functions as ma
from dj import development_tools  as log
from markov_functions.models import Book


@csrf_exempt
def ma_process(request):
    """ Send text to algorithm and return response """
    context_instance=RequestContext(request)
    if request.method == 'POST':
        try:
            # book = Book.objects.get(pk=(request.POST['bookid'])) 
            # marktext = book.file.read() # Should pass ID to markov and let it do the reading.

            markovedText = ma.markovify_text(
                bookIDs=request.POST['book_ids'],
                lines=request.POST['lines'],
                posEnabled=request.POST['posEnabled'],
                stateSize=int(request.POST['stateSize']), )
            return HttpResponse(markovedText)#.encode('utf-8'))
        except Exception as e:
            return HttpResponse(log.PrintException())
    return HttpResponse("Request was not sent as POST request.")

@csrf_exempt
def ma_processjson(request):
  """ Send text to algorithm and return response """
  context_instance=RequestContext(request)
  if request.method == 'POST':
    try:
      markovedText = ma.markovify_text(
        request.POST['lines'],
        request.POST['ulysses'],
        request.POST['erotic'],
        request.POST['grammar'],
        int(request.POST['stateSize']), )
      return HttpResponse(markovedText)
    except Exception as e:
      return HttpResponse(request)
  return HttpResponse("Request was not sent as POST request.")


#@csrf_exempt
#def steal_text(request):
#	response = steal_from_url(request.POST['url'])
#	return HttpResponse(response)

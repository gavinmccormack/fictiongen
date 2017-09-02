from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt ## Temporary
#from web_functions import steal_from_url
from django.template import RequestContext
import markov_functions.mk_functions as ma
from dj import development_tools  as log
from markov_functions.models import Book
import json


@csrf_exempt
def ma_process(request):
    """ Send text to algorithm and return response """
    context_instance=RequestContext(request)
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            print("Request Data")
            print(request_data)
            markovedText = ma.markovify_text(
                bookIDs=request_data['book_ids'],
                lines=request_data['lines'],
                posEnabled=request_data['posEnabled'],
                stateSize=request_data['stateSize'] )
            return HttpResponse(json.dumps(markovedText))#.encode('utf-8'))
        except Exception as e:
            return HttpResponse(log.PrintException())
    return HttpResponse("Request was not sent as POST request.")


#@csrf_exempt
#def steal_text(request):
#   response = steal_from_url(request.POST['url'])
#   return HttpResponse(response)

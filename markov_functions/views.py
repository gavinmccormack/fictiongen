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
            stateSize = int( request_data['stateSize'] )
            posEnabled = ( request_data['posEnabled'] == "True" ) # A bit iffy
            lines = int(request_data['lines'])
            fictionObj = ma.fictionObject(books=request_data['book_ids'], stateSize=stateSize )
            print("Fiction Object Created")
            markovedText = fictionObj.get_text( lines=lines, posEnabled=posEnabled)
            print("Text Markoved")
            return HttpResponse(json.dumps(markovedText))
        except Exception as e:
            return HttpResponse(log.PrintException())
    return HttpResponse("Request was not sent as POST request.")

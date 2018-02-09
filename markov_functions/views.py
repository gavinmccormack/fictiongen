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


@csrf_exempt # Not particularly concerned about illegitimate requests yet.
def ma_process(request):
    """ Send text to algorithm and return response """
    context_instance=RequestContext(request)
    if request.method == 'POST':
        try:
            # Populate variables
            request_data = json.loads(request.body)
            stateSize = int( request_data['stateSize'] )
            posEnabled = ( request_data['posEnabled'] == "True" ) # A bit iffy
            lines = int(request_data['lines'])
            paragraphs = int(request_data['paragraphs'])

            #Create instance and text 
            fictionObj = ma.fictionObject(books=request_data['book_ids'], stateSize=stateSize )
            markovedText = fictionObj.get_text( lines=lines, posEnabled=posEnabled, paragraphs=paragraphs)

            return HttpResponse(json.dumps(markovedText))
        except Exception as e:
            return HttpResponse(log.logException())
    return HttpResponse("Request was not sent as POST request.")

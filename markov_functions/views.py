from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt 
from django.template import RequestContext
import markov_functions.mk_functions as ma
from core import development_tools  as log
from markov_functions.models import Book
import json


@csrf_exempt # Not particularly concerned about illegitimate requests yet.
def ma_process(request):
    """ Send text to algorithm and return generated text """
    context_instance=RequestContext(request)
    if request.method == 'POST':
        try:
            # Populate variables. Nothing fancy here.
            request_body = request.body.decode('utf-8')
            request_data = json.loads(request_body)

            # I'm wondering about the logic of unpacking all of this JSON here. It maybe should just flow through in it's current state until it reaches an endpoint.
            # Something to do for spring cleaning.
        

            fictionObj = ma.fictionObject( request_data ) # Create the model of combined texts
            markovedText = fictionObj.get_text( request_data ) # Return the text

            data = json.dumps(markovedText)
            if data == "":
                data = "Insufficient text"
            return HttpResponse(data)
        except Exception as e:
            return HttpResponse(log.exception())
    return HttpResponse("Request was not sent as POST request.")

from curses.ascii import HT
import json
from copy import deepcopy
import re
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from .helpers.testing import bordered

def home(request:HttpRequest):
    return HttpResponse( 'hello')

def request_json(request:HttpRequest):
    bordered(
        json.dumps(
            vars(request).copy(),
            indent=2,
            default=lambda x: repr(x)
        )
    )
    # return HttpResponse('ok')
    return JsonResponse(
        vars(request).copy(),
        json_dumps_params=dict(
            indent=2,
            default=lambda x: repr(x)
        )
    )

def request_text(request:HttpRequest):
    return HttpResponse(
        json.dumps(
            vars(request).copy(),
            indent=2,
            default=lambda x: repr(x)
        ),
        content_type='text/plain'
    )

def response_json(request:HttpRequest):
    response = HttpResponse('the response')
    bordered(
        json.dumps(
            vars(response).copy(),
            indent=2,
            default=lambda x: repr(x)
        )
    )
    # return HttpResponse('ok')
    return JsonResponse(
        vars(response).copy(),
        json_dumps_params=dict(
            indent=2,
            default=lambda x: repr(x)
        )
    )


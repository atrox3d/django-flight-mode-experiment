from curses.ascii import HT
import json
from copy import deepcopy
import re
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from myapp.helpers.testing import request2dict


# Create your views here.

from . import models
from .helpers.testing import bordered, enable_output, disable_output

JSON_DUMP_PARAMS = dict(indent=2, default=lambda x: repr(x))

def home(request:HttpRequest):
    return HttpResponse( 'hello')

def request_json(request:HttpRequest):
    bordered(request2dict(request))
    # return HttpResponse('ok')
    return JsonResponse(
        vars(request).copy(),
        json_dumps_params=JSON_DUMP_PARAMS
    )

def request_text(request:HttpRequest):
    return HttpResponse(
        json.dumps(request2dict(request)),
        content_type='text/plain'
    )

def response_json(request:HttpRequest):
    response = HttpResponse('the response')
    bordered(request2dict(response))
    # return HttpResponse('ok')
    return JsonResponse(
        vars(response).copy(),
        json_dumps_params=JSON_DUMP_PARAMS
    )

def dishes(request:HttpRequest, dish:str):
    items = {
        'pasta': 'pasta is blah blah blah',
        'falafel': 'falafel is blah blah blah',
        'cheesecake': 'cheesecake is blah blah blah',
    }
    description = items[dish]

    return HttpResponse(f'<h2>dish</h2>{description}')

def menu(request:HttpRequest, dish:str):
    menuitem = models.Menu.objects.filter(menu_item=dish).first()
    bordered(menuitem)

    # needs queryset, no first()
    # data = serializers.serialize('json', menuitem)
    # return HttpResponse(data, content_type='application/json')

    # return ALL fields
    # return JsonResponse(menuitem.values().first())

    return JsonResponse(menuitem.dict())    # needs first




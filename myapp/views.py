from curses.ascii import HT
import json
from copy import deepcopy
import re
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from myapp.forms import InputForm, LogForm
from myapp.helpers.testing import request2dict, bordered


# Create your views here.

from .models import Menu
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
    menuitem = Menu.Menu.objects.filter(menu_item=dish).first()
    bordered(menuitem)
    bordered(menuitem.fieldnames())
    bordered(menuitem.dict())

    # needs queryset, no first()
    # data = serializers.serialize('json', menuitem)
    # return HttpResponse(data, content_type='application/json')

    # return ALL fields
    # return JsonResponse(menuitem.values().first())

    return JsonResponse(menuitem.dict())    # needs first

def form_view(request:HttpRequest):
    if request.method == 'POST':
        print(f'{request.POST = }')
    
    form = InputForm()
    context = dict(form=form)
    return render(request, 'home.html', context=context)

def logger_view(request:HttpRequest):
    if request.method == 'POST':
        print(f'logger_view | POST: {request.POST = }')
        form = LogForm(request.POST)
        if form.is_valid():
            print(f'logger_view | POST: saving')
            form.save()
        else:
            print(f'logger_view | POST: INVALID')
            print(form.errors.as_data()) # here you print errors to terminal
            print(form.errors) # here you print errors to terminal
    else:
        print(f'logger_view | GET')
        form = LogForm()
    
    context = dict(form=form)
    return render(request, 'home.html', context=context)
        


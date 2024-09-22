from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

from .helpers.testing import bordered

def home(request:HttpRequest):
    return HttpResponse(
            'hello', 
            content_type='text/plain'
    )

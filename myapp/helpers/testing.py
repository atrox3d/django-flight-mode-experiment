from django.http import HttpRequest


import json


BORDER_WIDTH = 30
BORDER_CHAR = '/ '
BORDER = BORDER_CHAR * BORDER_WIDTH
ENABLE_OUTPUT=True

def enable_output():
    global ENABLE_OUTPUT 
    ENABLE_OUTPUT= True

def disable_output():
    global ENABLE_OUTPUT 
    ENABLE_OUTPUT= False

def bordered(*args, border=BORDER, **kwargs):
    ''' prints args inside border '''
    if ENABLE_OUTPUT:
        print(BORDER)
        print(*args, **kwargs)
        print(BORDER)


def request2dict(
        request:HttpRequest,
        indent:int=2,
        default:str=lambda x: repr(x)
) -> dict:
    return json.dumps(
        vars(request).copy(),
        indent=indent,
        default=default
        )


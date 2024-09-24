BORDER_WIDTH = 30
BORDER_CHAR = '/ '
BORDER = BORDER_CHAR * BORDER_WIDTH

ENABLE_OUTPUT=True
# def bordered(fn):
#     def wrapped(*args, **kwargs):
#         print(BORDER)
#         res =  fn(*args, **kwargs)
#         print(BORDER)
#         return res
#     return wrapped

def enable_output():
    global ENABLE_OUTPUT 
    ENABLE_OUTPUT= True

def disable_output():
    global ENABLE_OUTPUT 
    ENABLE_OUTPUT= False

def bordered(*args, border=BORDER, **kwargs):
    if ENABLE_OUTPUT:
        print(BORDER)
        print(*args, **kwargs)
        print(BORDER)


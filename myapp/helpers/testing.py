BORDER_WIDTH = 30
BORDER_CHAR = '/ '
BORDER = BORDER_CHAR * BORDER_WIDTH

# def bordered(fn):
#     def wrapped(*args, **kwargs):
#         print(BORDER)
#         res =  fn(*args, **kwargs)
#         print(BORDER)
#         return res
#     return wrapped

def bordered(*args, border=BORDER, **kwargs):
    print(BORDER)
    print(*args, **kwargs)
    print(BORDER)


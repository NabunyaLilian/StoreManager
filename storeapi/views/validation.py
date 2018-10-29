from flask import request

def validate(a,b):
    
    if all(isinstance(x, str) for x in a) and all(isinstance(x, int) for x in b):
        return True
       

# def check_missing_field(fields):
#         if not fields:
#                 return 'missing fields'
                
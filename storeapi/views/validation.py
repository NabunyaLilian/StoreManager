from flask import request

def validate(a,b):
    
    if all(isinstance(x, str) for x in a) and all(isinstance(x, int) for x in b):
        return True
    True    


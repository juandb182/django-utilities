""" PlatziGram views"""

from django.http import HttpResponse

#Utilities
from datetime import datetime

#json
import json 

import pdb;

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M Hrs')
    return HttpResponse('Hello juan welcome to platzigram {now}'.format(now=str(now)))



def hi(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_int = sorted(numbers)

    data = {
        'status':'ok',
        'code':'200',
        'numbers':sorted_int,
        'message':'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data)
    ,content_type='application/json')


def welcome(request,name,level):
    if level < 18:
         message = 'Access Denied'
         return HttpResponse(message)
    else:
         message = 'Welcome {} lvl: {} '.format(name,level)
         return HttpResponse(message)

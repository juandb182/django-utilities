""" PlatziGram views"""

from django.http import HttpResponse

#Utilities
from datetime import datetime

import pdb;

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M Hrs')
    return HttpResponse('Hello juan welcome to platzigram {now}'.format(now=str(now)))



def hi(request):
    print(request)
    return HttpResponse(number)
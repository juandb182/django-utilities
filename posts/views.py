""" Posts views """

#Django
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime



posts = [
    {
        'title':'Mont blanc',
        'user': {
            'name':'Jessica Cortez',
            'picture':'https://pbs.twimg.com/media/CqS2i-nXYAAl5d9?format=jpg&name=large'
        },
        'media': 'https://pbs.twimg.com/media/Cwl1CbcXAAANPU1?format=jpg&name=large',
        'description': 'a star war pixel arte incredible',
        'timestamp':datetime.now().strftime('%b %dth %Y - %H:%M Hrs'),
    },
    {
        'title':'Lex ipsum',
        'user': {
            'name':'Octo Hatred',
            'picture':'https://pbs.twimg.com/media/Cpx4mhTWYAAauKc?format=jpg&name=large'
        },
        'media':'https://pbs.twimg.com/media/CqS2i-nXYAAl5d9?format=jpg&name=large',
        'description':'Different photo today',
        'timestamp':datetime.now().strftime('%b %dth %Y - %H:%M Hrs'),
    },
     {
        'title':'Ardu Ino',
        'user': {
            'name':'Dert Exinos',
            'picture':'https://pbs.twimg.com/media/Cwl1CbcXAAANPU1?format=jpg&name=large'
        },
        'media':'https://pbs.twimg.com/media/Cpx4mhTWYAAauKc?format=jpg&name=large',
        'description':'Bep Bep Robot',
        'timestamp':datetime.now().strftime('%b %dth %Y - %H:%M Hrs'),
    },
]

# Create your views here.
def list_posts(request):
    
    return render(request,'feed.html',{'posts':posts})
  
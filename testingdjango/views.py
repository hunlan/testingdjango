'''
Created on Oct 3, 2012

@author: hunlan
'''
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
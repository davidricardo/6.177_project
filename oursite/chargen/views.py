"""
This file controls which http responses and html pages are shown.

Functions here should take their input from urls.py and return an 
HttpResponse object.

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
or at https://docs.djangoproject.com/en/1.6/topics/http/views/
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, RequestContext, loader

from character import VARS_TO_PASS

def index(request):
    #the template to load
    template = loader.get_template('chargen/index.html')
    #contexts are a set of variable => value pairs that a template uses to generate a page.
    context = Context(VARS_TO_PASS)
    return HttpResponse(template.render(context))
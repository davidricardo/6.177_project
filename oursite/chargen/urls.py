"""
Urls that are passed from oursite/oursite/urls.py will go here.

Functions in here should take a url as an argument and call
the appropriate function in oursite/chargen/views.py.

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
or at https://docs.djangoproject.com/en/1.6/ref/urls/.
"""

from django.conf.urls import patterns, url
from chargen import views

# message = character.TEST_MESSAGE

urlpatterns = patterns('',
    #not sure why this regex only matches the empty string?
    url(r'^$', views.index, name='index')
    )
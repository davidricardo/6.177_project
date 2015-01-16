"""
Urls for the site will be passed here first, and this passes
them on to chargen/urls.py. 

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oursite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

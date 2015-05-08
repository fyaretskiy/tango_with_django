__author__ = 'feliks'
"""
urls.py for url mapping
"""

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))

"""
Created : 14th November 2017
@author : Reshma Konjari
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

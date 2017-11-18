# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

"""
Created :14 November 2017
@author : Reshma Konjari
"""

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> This is a music app Homepage</h1>")

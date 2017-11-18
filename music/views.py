# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

"""
Created :14 November 2017
@author : Reshma Konjari
"""

from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):

    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    # context = {
    #     'all_albums': all_albums,
    # }

    # ===============  Commenting out the HTML code ===============
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    # ==============================================================

    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    # ===============  Commenting out the httpresponse code ===============
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")
    # ==============================================================
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})

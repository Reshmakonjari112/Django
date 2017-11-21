"""
Created : 14th November 2017
@author : Reshma Konjari
"""

from django.conf.urls import url
from . import views
app_name = 'music'


urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/712/
    # <------712 is an album_id----------->
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.detail, name='favorite'),

]

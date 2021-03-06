from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.music_tracks, name='music_tracks'),
    url(r'^(?P<id>\d+)/$', views.music_track, name='music_track'),
    url(r'^download/(?P<id>\d+)/$', views.download_private_track, name='download_private_track'),
]

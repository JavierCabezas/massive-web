from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.music_packs, name='music_packs'),
    url(r'^(?P<id>\d+)/$', views.music_pack, name='music_pack'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^music_packs', views.music_packs, name='music_packs'),
    url(r'^music_pack/(?P<id>\d+)/$', views.music_pack, name='music_pack'),
]
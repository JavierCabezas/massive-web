from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts', views.posts, name='posts'),
    url(r'^post/(?P<id>\d+)/$', views.post, name='post')
]
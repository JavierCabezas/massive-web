from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/(?P<limit>\d+)/$', views.posts, name='posts_with_limit'),
    url(r'^posts', views.posts, name='posts'),
    url(r'^post/(?P<id>\d+)/$', views.post, name='post')
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.new, name='new'),
    url(r'^create_cart', views.create_cart, name='create_cart'),
]

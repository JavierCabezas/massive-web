from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^parents', views.parents, name='parents'),
]
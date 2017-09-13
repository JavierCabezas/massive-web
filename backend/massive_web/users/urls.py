from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_google_user', views.create_google_user, name='create_google_user'),
    url(r'^get_user', views.get_user, name='get_user'),
    url(r'^login', views.login, name='login'),
]
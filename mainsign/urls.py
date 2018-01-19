from django.conf.urls import url

from mainsign import views

urlpatterns = [
    url(r'^mainsign', views.mainsign, name='mainsign'),
]
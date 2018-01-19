from django.conf.urls import url

from company import views

urlpatterns = [
    url(r'^company', views.company, name='company'),
]
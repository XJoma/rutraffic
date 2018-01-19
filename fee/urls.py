from django.conf.urls import url

from fee import views

urlpatterns = [
    url(r'^fee/', views.fee, name='fee'),

]
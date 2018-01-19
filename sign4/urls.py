from django.conf.urls import url

from sign4 import views

urlpatterns = [
    url(r'^sign4/', views.sign4, name='sign4'),
    url(r'^post4/(?P<id>\w+)/$', views.post_single4, name='post_single4'),
    url(r'^add4/$', views.post_new4, name='post_new4'),
    url(r'^post4/(?P<id>[0-9]+)/edit/$', views.post_edit4, name='post_edit4'),
    url(r'^post4/(?P<id>[0-9]+)/delete/$', views.post_delete4, name='post_delete4'),
]
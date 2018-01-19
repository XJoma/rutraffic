from django.conf.urls import url

from sign3 import views

urlpatterns = [
    url(r'^sign3/', views.sign3, name='sign3'),
    url(r'^post3/(?P<id>\w+)/$', views.post_single3, name='post_single3'),
    url(r'^add3/$', views.post_new3, name='post_new3'),
    url(r'^post3/(?P<id>[0-9]+)/edit/$', views.post_edit3, name='post_edit3'),
    url(r'^post3/(?P<id>[0-9]+)/delete/$', views.post_delete3, name='post_delete3'),
]
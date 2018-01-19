from django.conf.urls import url

from sign2 import views

urlpatterns = [
    url(r'^sign2/', views.sign2, name='sign2'),
    url(r'^post2/(?P<id>\w+)/$', views.post_single2, name='post_single2'),
    url(r'^add2/$', views.post_new2, name='post_new2'),
    url(r'^post2/(?P<id>[0-9]+)/edit/$', views.post_edit2, name='post_edit2'),
    url(r'^post2/(?P<id>[0-9]+)/delete/$', views.post_delete2, name='post_delete2'),
]
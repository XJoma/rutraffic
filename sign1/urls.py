from django.conf.urls import url

from sign1 import views

urlpatterns = [
    url(r'^sign1/', views.sign1, name='sign1'),
    url(r'^post1/(?P<id>\w+)/$', views.post_single1, name='post_single1'),
    url(r'^add1/$', views.post_new1, name='post_new1'),
    url(r'^post1/(?P<id>[0-9]+)/edit/$', views.post_edit1, name='post_edit1'),
    url(r'^post1/(?P<id>[0-9]+)/delete/$', views.post_delete1, name='post_delete1'),
]
from django.conf.urls import url

from sign import views

urlpatterns = [
    url(r'^sign/', views.sign, name='sign'),
    url(r'^post/(?P<id>\d+)/$', views.post_single, name='post_single'),
    url(r'^add/$', views.post_new, name='post_new'),
    url(r'^post/(?P<id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]
"""rutraffic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^sign/', include('sign.urls')),
    url(r'^sign1/', include('sign1.urls')),
    url(r'^sign2/', include('sign2.urls')),
    url(r'^sign3/', include('sign3.urls')),
    url(r'^sign4/', include('sign4.urls')),
    url(r'^fee/', include('fee.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^mainsign/', include('mainsign.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

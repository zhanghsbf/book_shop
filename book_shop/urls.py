"""book_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from post.views import *
from yonghu.views import *
from backmanage.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^user/', include('yonghu.urls', namespace='yonghu')),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^transfer/$', login_required_transfer),
    url(r'^buy/', include('buy.urls', namespace='buy')),
    url(r'^manage/', include('backmanage.urls', namespace='manage')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""midnight URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'', include('midnight_news.urls', namespace='midnight_news')),
    url(r'', include('midnight_catalog.urls', namespace='midnight_catalog')),
    url(r'^$', 'midnight_main.views.main_page'),
    url(r'', include('midnight_main.urls', namespace='midnight_main')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/(?P<section_slug>[A-z0-9_-]+)/(?P<slug>[A-z0-9_-]+)/$', views.detail, name='news_detail'),
    url(r'^news/(?P<slug>[A-z0-9_-]+)/$', views.index, name='news_list'),
    url(r'^news/$', views.index, name='news_list'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^catalog/(?P<section_slug>[A-z0-9_-]+)/(?P<slug>[A-z0-9_-]+)/$', views.detail, name='catalog_detail'),
    url(r'^catalog/(?P<slug>[A-z0-9_-]+)/$', views.index, name='catalog_list'),
    url(r'^catalog/$', views.index, name='catalog_list'),
]

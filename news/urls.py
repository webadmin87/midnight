from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/detail/(?P<slug>\w+)/$', views.detail, name='news_detail'),
    url(r'^news/(?P<slug>\w+)/$', views.index, name='news_list'),
    url(r'^news/$', views.index, name='news_list'),
]

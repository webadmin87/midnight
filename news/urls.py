from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^news/$', views.index, name='news_list'),
]

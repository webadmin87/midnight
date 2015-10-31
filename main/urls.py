from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^feedback/$', views.feedback, name='page_feedback'),
    url(r'^(?P<slug>\w+)/$', views.index, name='page_detail'),
]

from django.conf.urls import url

from midnight_main.views import CommentView
from midnight_news import models
from . import views, forms

urlpatterns = [
    url(r'^news/(?P<section_slug>[A-z0-9_-]+)/(?P<slug>[A-z0-9_-]+)/$', views.detail, name='news_detail'),
    url(r'^news/(?P<slug>[A-z0-9_-]+)/$', views.index, name='news_list'),
    url(r'^news/$', views.index, name='news_list'),
    url(r'^news-comments/$', CommentView.as_view(model_cls=models.NewsComment, form_cls=forms.NewsCommentForm), name='news_comments'),
]

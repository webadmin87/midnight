from django.conf.urls import url
from midnight_main.views import CommentView
from . import views, forms, models

urlpatterns = [
    url(r'^catalog/(?P<section_slug>[A-z0-9_-]+)/(?P<slug>[A-z0-9_-]+)/$', views.detail, name='catalog_detail'),
    url(r'^catalog/(?P<slug>[A-z0-9_-]+)/$', views.index, name='catalog_list'),
    url(r'^catalog/$', views.index, name='catalog_list'),
    url(r'^product-comments/$', CommentView.as_view(model_cls=models.ProductComment, form_cls=forms.ProductCommentForm), name='product_comments'),
]

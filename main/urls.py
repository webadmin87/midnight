from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from midnight import mptt_urls

urlpatterns = [
    url(r'^accounts/profile/$', login_required(views.UpdateProfile.as_view()), name='user_profile'),
    url(r'^feedback/$', views.feedback, name='page_feedback'),
    url(r'^(?P<path>.*)/$', mptt_urls.View(model='main.models.Page', view='main.views.pages', slug_field='slug'), name='page_detail'),
]

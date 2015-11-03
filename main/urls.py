from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', login_required(views.UpdateProfile.as_view()), name='user_profile'),
    url(r'^feedback/$', views.feedback, name='page_feedback'),
    url(r'^(?P<slug>\w+)/$', views.index, name='page_detail'),
]

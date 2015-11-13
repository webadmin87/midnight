from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views, models, forms
from midnight import mptt_urls

urlpatterns = [
    url(r'^accounts/profile/$', login_required(views.UpdateProfile.as_view()), name='user_profile'),
    url(r'^feedback/$', views.FeedbackView.as_view(form_cls=forms.Feedback), name='page_feedback'),
    url(r'^page-comments/$', views.CommentView.as_view(model_cls=models.PageComment, form_cls=forms.PageCommentForm), name='page_comments'),
    url(r'^(?P<path>.*)/$', mptt_urls.View(model='main.models.Page', view='main.views.pages', slug_field='slug'), name='page_detail'),
]

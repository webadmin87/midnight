from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from main.forms import Feedback, Profile
from main.mailer import send_templated_mail
from main.services import get_page_tpl_ctx, get_object_comments, post_comment
from .models import Page, AppUser
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View


class UpdateProfile(UpdateView):
    model = AppUser
    form_class = Profile
    template_name = 'main/users/appuser_update_form.html'

    def get_success_url(self):
            return reverse('main:user_profile')

    def form_valid(self, form):

        if form.data['password_change']:
            user = form.save(commit=False)
            user.set_password(form.data['password_change'])
            update_session_auth_hash(self.request, user)

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def pages(request, path=None, instance=None):

    if instance and instance.active:
        p = instance
    else:
        raise Http404()

    return render(request, 'main/pages/pages.html', get_page_tpl_ctx(p, request))


def main_page(request):
    p = get_object_or_404(Page, slug='main', active=True)
    return render(request, 'main/pages/pages.html', get_page_tpl_ctx(p, request))


@require_POST
def feedback(request):

    form = Feedback(request.POST)

    if form.is_valid():
        send_templated_mail('main/mails/feedback.html', _('Feedback message'), form)
        status = 200
    else:
        status = 422

    return render(request, 'main/tags/ajax_form_body.html', {'form': form}, status=status)


class CommentView(View):

    model_cls = None

    form_cls = None

    list_tpl = 'main/tags/comments_list.html'

    form_tpl = 'main/tags/comments_form_body.html'

    def get(self, request):
        comments = get_object_comments(self.model_cls, request.GET.get('id', 0))
        return render(request, self.list_tpl, {'comments': comments})

    def post(self, request):

        form = self.form_cls(request.POST)

        res = post_comment(form, request.user)

        status = 200 if res else 422

        return render(request, self.form_tpl, {'form': form}, status=status)

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from main.forms import Feedback, Profile
from main.mailer import send_templated_mail
from midnight.components import MetaSeo
from .models import Page, AppUser
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView
from django.contrib.auth import update_session_auth_hash


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

        return super(UpdateProfile, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def index(request, slug='main'):

    p = get_object_or_404(Page, slug=slug, active=True)

    text = Template(p.text).render(Context())

    meta = MetaSeo(p)

    return render(request, 'main/pages/index.html', {'page': p, 'text': text, 'meta': meta})


@require_POST
def feedback(request):

    form = Feedback(request.POST)

    if form.is_valid():
        send_templated_mail('main/mails/feedback.html', _('Feedback message'), form)
        status = 200
    else:
        status = 422

    return render(request, 'main/tags/ajax_form_body.html', {'form': form}, status=status)

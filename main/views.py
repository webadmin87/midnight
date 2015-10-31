from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from main.forms import Feedback
from main.mailer import send_templated_mail
from midnight.components import MetaSeo
from .models import Page
from django.template import Template, Context
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


def index(request, slug='main'):

    p = get_object_or_404(Page, slug=slug, active=True)

    text = Template(p.text).render(Context())

    meta = MetaSeo(p)

    return render(request, 'main/pages/index.html', {'page': p, 'text': text, 'meta': meta})


def feedback(request):

    if request.method == 'POST':

        form = Feedback(request.POST)

        if form.is_valid():
            send_templated_mail('main/mails/feedback.html', _('Feedback message'), form)
            messages.add_message(request, messages.SUCCESS, _('Message send success'))
            return HttpResponseRedirect(reverse(viewname='main:page_feedback'))

    else:
        form = Feedback()

    return render(request, 'main/pages/feedback.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from main.forms import Feedback
from main.mailer import send_templated_mail
from midnight.components import MetaSeo
from .models import Page
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST


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

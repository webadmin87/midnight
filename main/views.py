from django.shortcuts import render, get_object_or_404
from midnight.components import MetaSeo
from .models import Page
from django.template import Template, Context


def index(request, slug='main'):

    p = get_object_or_404(Page, slug=slug, active=True)

    text = Template(p.text).render(Context())

    meta = MetaSeo(p)

    return render(request, 'main/pages/index.html', {'page': p, 'text': text, 'meta': meta})



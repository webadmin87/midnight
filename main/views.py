from django.shortcuts import render, get_object_or_404
from .models import Page
from django.template import Template, Context


def index(request, slug='main'):

    p = get_object_or_404(Page, slug=slug)

    text = Template(p.text).render(Context())

    return render(request, 'main/pages/index.html', {'page': p, 'text': text})



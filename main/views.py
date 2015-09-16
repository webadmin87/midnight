from django.shortcuts import render, get_object_or_404
from .models import Page


def index(request, slug='main'):

    p = get_object_or_404(Page, slug=slug)

    return render(request, 'main/pages/index.html', {'page': p})



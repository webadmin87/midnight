from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Page

def index(request, slug='main'):
	p = get_object_or_404(Page, slug=slug)
	return render(request, 'pages/index.html', {'page': p})



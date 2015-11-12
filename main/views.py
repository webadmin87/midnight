from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from main.forms import Feedback, Profile, PageCommentForm
from main.mailer import send_templated_mail
from midnight.components import MetaSeo
from .models import Page, AppUser, PageComment
from django.template import Template, Context
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

        return super(UpdateProfile, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def pages(request, path=None, instance=None):

    if instance and instance.active:
        p = instance
    else:
        raise Http404()

    text = Template(p.text).render(Context())
    meta = MetaSeo(p)
    comments = PageComment.objects.root_nodes().filter(obj__id=p.id).all()
    form = PageCommentForm(initial={'obj': p})
    return render(request, 'main/pages/pages.html', {'page': p, 'comments': comments, 'form': form, 'text': text, 'meta': meta, 'crumbs': p.get_breadcrumbs()})


def main_page(request):
    p = get_object_or_404(Page, slug='main', active=True)
    text = Template(p.text).render(Context())
    meta = MetaSeo(p)
    comments = PageComment.objects.root_nodes().filter(obj__id=p.id).all()
    form = PageCommentForm(initial={'obj': p})
    return render(request, 'main/pages/pages.html', {'page': p, 'comments': comments, 'form': form, 'text': text, 'meta': meta})


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

    def __init__(self, model_cls, form_cls):
        self.model_cls = model_cls
        self.form_cls = form_cls

    def get(self, request):
        comments = self.model_cls.objects.root_nodes().filter(obj__id=request.GET.id).all()
        return render(request, 'main/tags/comments_list.html', {'comments': comments})

    def post(self, request):

        form = self.form_cls(request.POST)

        if form.is_valid():
            model = form.save(commit=False)
            model.author = request.user
            model.save()
            status = 200
        else:
            status = 422

        return render(request, 'main/tags/comments_form_body.html', {'form': form}, status=status)

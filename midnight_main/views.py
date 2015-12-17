from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from midnight_main.forms import Feedback, Profile
from midnight_main.mailer import send_templated_mail
from midnight_main.services import get_page_tpl_ctx, get_object_comments, post_comment
from .models import Page, AppUser
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import UpdateView
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View


class UpdateProfile(UpdateView):
    """
    Изменение профиля пользователя
    """

    model = AppUser
    form_class = Profile
    template_name = 'midnight_main/users/appuser_update_form.html'

    def get_success_url(self):
            return reverse('midnight_main:user_profile')

    def form_valid(self, form):

        if form.data['password_change']:
            user = form.save(commit=False)
            user.set_password(form.data['password_change'])
            update_session_auth_hash(self.request, user)

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def pages(request, path=None, instance=None):
    """
    Представление для отображения текстовых страниц
    :param request: запрос
    :param path: адрес
    :param instance: страница
    :return:
    """

    if instance and instance.active:
        p = instance
    else:
        raise Http404()

    return render(request, p.tpl, get_page_tpl_ctx(p, request))


def main_page(request):
    """
    Представление для отображения главной страницы
    :param request: запрос
    :return:
    """
    p = get_object_or_404(Page, slug='main', active=True)
    return render(request, p.tpl, get_page_tpl_ctx(p, request))


class FeedbackView(View):
    """
    Представление для обратной связи
    """

    form_cls = None

    subject = 'Feedback message'

    mail_tpl = 'midnight_main/mails/feedback.html'

    form_tpl = 'midnight_main/tags/ajax_form_body.html'

    def post(self, request):

        form = self.form_cls(request.POST)

        if form.is_valid():
            send_templated_mail(self.mail_tpl, _(self.subject), form)
            status = 200
        else:
            status = 422

        return render(request, self.form_tpl, {'form': form}, status=status)


class CommentView(View):
    """
    Представление для добавления и отображения комментариев
    """

    model_cls = None
    """Класс модели комментариев"""

    form_cls = None
    """Класс формы добавления комментариев"""

    list_tpl = 'midnight_main/tags/comments_list.html'

    form_tpl = 'midnight_main/tags/comments_form_body.html'

    def get(self, request):
        comments = get_object_comments(self.model_cls, request.GET.get('id', 0))
        return render(request, self.list_tpl, {'comments': comments})

    def post(self, request):

        form = self.form_cls(request.POST)

        if request.user.is_authenticated():
            del form.fields['captcha']

        res = post_comment(form, request.user)

        status = 200 if res else 422

        return render(request, self.form_tpl, {'form': form}, status=status)

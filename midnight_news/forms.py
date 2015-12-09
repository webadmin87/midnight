from captcha.fields import CaptchaField
from django import forms
from django.utils.translation import ugettext_lazy as _

from midnight_news.models import NewsComment


class NewsCommentForm(forms.ModelForm):
    """
    Форма для добавления комментария к новости
    """

    captcha = CaptchaField(label=_('Captcha'))

    class Meta:
        model = NewsComment
        exclude = ('active', 'author')
        widgets = {
            'parent': forms.HiddenInput,
            'obj': forms.HiddenInput,
        }

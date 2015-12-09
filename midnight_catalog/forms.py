from captcha.fields import CaptchaField
from django import forms
from .models import ProductComment
from django.utils.translation import ugettext_lazy as _


class ProductCommentForm(forms.ModelForm):
    """
    Форма добавления комментария к товару
    """

    captcha = CaptchaField(label=_('Captcha'))

    class Meta:
        model = ProductComment
        exclude = ('active', 'author')
        widgets = {
            'parent': forms.HiddenInput,
            'obj': forms.HiddenInput,
        }
from captcha.fields import CaptchaField
from django import forms
from django.utils.translation import ugettext_lazy as _


class Feedback(forms.Form):

    name = forms.CharField(label=_('Name'), max_length=255)

    email = forms.EmailField(label=_('Email'), max_length=64)

    phone = forms.CharField(label=_('Phone'), max_length=11, required=False)

    text = forms.CharField(widget=forms.Textarea, label=_('Text'))

    captcha = CaptchaField(label=_('Captcha'))

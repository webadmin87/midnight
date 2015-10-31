from django import forms
from django.utils.translation import ugettext_lazy as _


class Feedback(forms.Form):

    name = forms.CharField(label=_('name'), max_length=255)

    email = forms.EmailField(label=_('email'), max_length=64)

    phone = forms.CharField(label=_('phone'), max_length=11, required=False)

    text = forms.CharField(widget=forms.Textarea)

from captcha.fields import CaptchaField
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from main.models import AppUser
from midnight.widgets import AdminImageWidget


class Feedback(forms.Form):

    name = forms.CharField(label=_('Name'), max_length=255)

    email = forms.EmailField(label=_('Email'), max_length=64)

    phone = forms.CharField(label=_('Phone'), max_length=11, required=False)

    text = forms.CharField(widget=forms.Textarea, label=_('Text'))

    captcha = CaptchaField(label=_('Captcha'))


class Profile(forms.ModelForm):

    password_change = forms.CharField(required=False, widget=forms.PasswordInput, min_length=6)

    password_change_confirm = forms.CharField(required=False, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        password_change = cleaned_data.get("password_change")
        password_change_confirm = cleaned_data.get("password_change_confirm")
        if password_change != password_change_confirm:
            raise forms.ValidationError("Passwords must be identical.")

        return cleaned_data

    class Meta:
        model = AppUser
        fields = ('username', 'password_change', 'password_change_confirm', 'image', 'email', 'first_name', 'last_name', 'phone')
        widgets = {
            'image': AdminImageWidget,
        }

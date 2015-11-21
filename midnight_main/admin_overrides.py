from django.apps import apps
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

# Переименовываем регистрацию
from precise_bbcode.models import BBCodeTag, SmileyTag

apps.get_app_config('registration').verbose_name = _("Registration")

# Отключаем приложение bb кодов
admin.site.unregister(BBCodeTag)
admin.site.unregister(SmileyTag)

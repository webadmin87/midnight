from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BannersConfig(AppConfig):

    name = 'banners'

    verbose_name = _('Banners')

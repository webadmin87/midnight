from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CatalogConfig(AppConfig):

    name = 'midnight_catalog'

    verbose_name = _('Catalog')

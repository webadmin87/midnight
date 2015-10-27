from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NewsConfig(AppConfig):

    name = u'news'

    verbose_name = _(u'News')

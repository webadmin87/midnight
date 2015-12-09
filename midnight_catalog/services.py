from django.conf import settings
from django.db.models import Prefetch
from midnight_catalog.models import Product, ParamValue


def get_all(slug=None):
    """
    Возвращает QuerySet содержащий выборку товаров
    :param slug: символьный код категории каталога, если не задан выбираются товары в не зависимости от категории
    :return:
    """
    if slug is None:
        q = Product.objects.published()
    else:
        q = Product.objects.published().filter(sections__slug=slug)

    if getattr(settings, 'MIDNIGHT_CATALOG_PREFETCH_PARAMS', False):
        q = q.prefetch_related(Prefetch("paramvalue_set", queryset=ParamValue.objects.published().order_by('sort').prefetch_related("param")))

    q = q.prefetch_related('sections').order_by('sort', '-id')

    return q.all()


def get_one(slug):
    """
    Возвращает один товар
    :param slug: символьный код товара
    :return:
    """
    item = Product.objects.published()\
        .prefetch_related(Prefetch("paramvalue_set", queryset=ParamValue.objects.published().order_by('sort').prefetch_related("param")))\
        .filter(slug=slug).first()
    return item

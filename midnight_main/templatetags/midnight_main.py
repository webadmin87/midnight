from django import template
from midnight_main.models import Menu, PhotoAlbum, IncludeArea
from django.core.urlresolvers import reverse
import uuid
from django.utils.module_loading import import_string

from midnight_main.services import mark_current_menus

register = template.Library()


def show_menu(context, slug, level=2, **kwargs):
    """
    Тег для подключения меню

    Пример использования::

        {% show_menu 'menu_slug' 2 class='menu-class' %}

    :param context: контекст шаблона
    :param slug: символьный код родительского пункта меню
    :param level: максимальный уровень вложенности
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """
    try:
        menu = Menu.objects.published().get(slug=slug)
        menus = menu.get_descendants().published().all()
        mark_current_menus(menus, context['request'].path_info)
        max_level = menu.level + level
        return {'menus': menus, 'max_level': max_level, 'data': kwargs}
    except Menu.DoesNotExist:
        return None

register.inclusion_tag(file_name='midnight_main/tags/show_menu.html', takes_context=True, name='show_menu')(show_menu)


def show_gallery(slug, size="100x100", crop="center", **kwargs):
    """
    Тег отображения фотогалереи

    Пример использования::

        {% show_gallery "gallery-slug" "150x110" "center" class='gallery-class' %}

    :param slug: символьный код фотогалереи
    :param size: размер
    :param crop: параметры кропа
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """

    try:
        album = PhotoAlbum.objects.published().get(slug=slug)
        photos = album.photo_set.published().order_by('sort').all()
        return {'album': album, 'photos': photos, 'size': size, 'crop': crop, 'data': kwargs}
    except PhotoAlbum.DoesNotExist:
        return None

register.inclusion_tag(file_name='midnight_main/tags/show_gallery.html', name='show_gallery')(show_gallery)


@register.simple_tag()
def show_area(slug):
    """
    Подключение включаемой области

    Пример использования::

        {% show_area "area_slug" %}

    :param slug: символьный код области
    :return:
    """
    try:
        area = IncludeArea.objects.published().get(slug=slug)
        return area.text
    except IncludeArea.DoesNotExist:
        return ""


def ajax_form(cls_name, view_name, modal=False, tag_id=None):
    """
    Подключение Ajax формы

    Пример использования (обратная связь)::

        {% ajax_form 'midnight_main.forms.Feedback' 'midnight_main:page_feedback' tag_id='feedback_form' modal=True %}

    :param cls_name: имя класса формы
    :param view_name: имя представления для обработки формы
    :param modal: форма предназначена для отображаения в fancybox и изначально скрыта
    :param tag_id: идентификатор оборачивающего тега
    :return:
    """
    if tag_id is None:
        tag_id = uuid.uuid4().hex[:6].lower()
    form = import_string(cls_name)()
    url = reverse(view_name)
    return {'form': form, 'url': url, 'modal': modal, 'id': tag_id}

register.inclusion_tag(file_name='midnight_main/tags/ajax_form.html', name='ajax_form')(ajax_form)


def user_info(context):
    """
    Отображает информацию о текущем авторизованом пользователе, либо ссылки на авторизацию и регистрацию

    Пример использования::

        {% user_info %}

    :param context: контекст
    :return:
    """
    request = context['request']
    return {'user': request.user}

register.inclusion_tag(file_name='midnight_main/tags/user_info.html', takes_context=True, name='user_info')(user_info)


def breadcrumbs(crumbs, **kwargs):
    """
    Тег для отображения хлебхых крошек

    Пример использования::

        {% breadcrumbs crumbs class='breadcrumb' %}

    :param crumbs: список хлебных крошек. [{'label': 'Crumb label', 'url': '/crumb-url/'}, ... ]
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """
    return {'crumbs': crumbs, 'data': kwargs}

register.inclusion_tag(file_name='midnight_main/tags/breadcrumbs.html', name='breadcrumbs')(breadcrumbs)


def comments_block(comments, form, obj, url, **kwargs):
    """
    Тег для отображения блока комментариев

    Пример использования (комментарии к текстовой странице)::

        {% comments comments comments_form page "midnight_main:page_comments" %}

    :param comments: список комментариев
    :param form: форма добавления комментария
    :param obj: объект к которому привязаны комментарии
    :param url: имя представления обрабатывающего создание и получение комментариев
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """

    data = kwargs

    if 'class' in data:
        data['class'] += ' comments-block'
    else:
        data['class'] = 'comments-block'

    return {'comments': comments, 'form': form, 'url': url, 'obj': obj, 'data': data}

register.inclusion_tag(file_name='midnight_main/tags/comments.html', name='comments')(comments_block)


def search_simple_form(context):
    """
    Форма поиска

    Пример использования::

        {% search_simple_form %}

    :param context: контекст
    :return:
    """
    return {'query': context['request'].GET.get('q', '')}

register.inclusion_tag(file_name='midnight_main/tags/search.html', takes_context=True, name='search_simple_form')(search_simple_form)

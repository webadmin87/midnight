from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import Template, Context

from midnight_main.forms import PageCommentForm
from midnight_main.models import PageComment, Page
from midnight_main.components import MetaSeo


def get_page_tpl_ctx(page, request):
    text = Template(page.text).render(Context())
    meta = MetaSeo(page)
    comments = get_object_comments(PageComment, page.id)
    comments_form = PageCommentForm(initial=get_comment_init(request, page))
    if page.slug == Page.MAIN_SLUG:
        crumbs = None
    else:
        crumbs = page.get_breadcrumbs()
    return {'page': page, 'comments': comments, 'comments_form': comments_form, 'text': text, 'meta': meta, 'crumbs': crumbs}


def get_comment_init(request, obj):
    if request.user.is_authenticated():
        init = {'obj': obj, 'username': request.user.username, 'email': request.user.email}
    else:
        init = {'obj': obj}
    return init


def get_object_comments(model_cls, obj_id):
    return model_cls.objects.filter(obj__id=obj_id).all()


def post_comment(form, user):
    if form.is_valid():
        model = form.save(commit=False)
        if user.is_authenticated():
            model.author = user
        model.save()
        return True
    else:
        return False


def save_formset_with_author(formset, user):
    instances = formset.save(commit=False)
    for obj in formset.deleted_objects:
        obj.delete()
    for instance in instances:
        if user.is_authenticated() and hasattr(instance, 'author'):
            instance.author = user
        instance.save()
    formset.save_m2m()


def get_by_page(query, page, page_size):

    pager = Paginator(query, page_size)

    try:
        models = pager.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        models = pager.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        models = pager.page(pager.num_pages)

    return models


def mark_current_menus(menus, path_info):
    for menu in menus:
        if menu.get_absolute_url() == "/":
            menu.is_current = menu.get_absolute_url() == path_info
        else:
            menu.is_current = path_info.find(menu.get_absolute_url()) == 0

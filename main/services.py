from django.template import Template, Context

from main.forms import PageCommentForm
from main.models import PageComment, Page
from midnight.components import MetaSeo


def get_page_tpl_ctx(page):
    text = Template(page.text).render(Context())
    meta = MetaSeo(page)
    comments = get_object_comments(PageComment, page.id)
    comments_form = PageCommentForm(initial={'obj': page})
    if page.slug == Page.MAIN_SLUG:
        crumbs = None
    else:
        crumbs = page.get_breadcrumbs()
    return {'page': page, 'comments': comments, 'comments_form': comments_form, 'text': text, 'meta': meta, 'crumbs': crumbs}


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

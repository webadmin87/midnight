from main.models import *
from django.contrib import admin
from midnight.base_models import BaseAdmin, BaseAdminTree


class PageAdmin(BaseAdmin):

    fieldsets = [
        (None, {'fields':  ['title', 'slug', 'active', 'text']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    list_display = ('title', 'slug', 'active')


admin.site.register(Page, PageAdmin)


class MenuAdmin(BaseAdminTree):

    fields = ['parent', 'active', 'title', 'link', 'slug', 'target', 'cls', 'sort']

    list_display = ('title', 'link', 'active', 'sort')

    pass

admin.site.register(Menu, MenuAdmin)

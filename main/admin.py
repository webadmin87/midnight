from main.models import *
from django.contrib import admin
from midnight.base_models import BaseAdmin


class PageAdmin(BaseAdmin):

    fields = ['title', 'slug', 'active', 'text']

    list_display = ('title', 'slug', 'active')


admin.site.register(Page, PageAdmin)

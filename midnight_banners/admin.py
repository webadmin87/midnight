from django.contrib import admin
from midnight_main.admin import BaseAdmin
from midnight_main.services import save_formset_with_author
from .models import *


class BannerInline(admin.StackedInline):

    exclude = ['author']

    model = Banner

    extra = 3

    ordering = ('sort',)


class BannerPlaceAdmin(BaseAdmin):

    exclude = ['author']

    list_display = ('title', 'id', 'slug', 'active')

    inlines = [BannerInline]

    list_filter = ('active',)

    search_fields = ('id', 'title', 'slug',)

    def save_formset(self, request, form, formset, change):
        save_formset_with_author(formset, request.user)


admin.site.register(BannerPlace, BannerPlaceAdmin)


from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.translation import ugettext_lazy as _

from midnight_main.models import *
from midnight_main.widgets import AdminImageWidget


class BaseAdminAbstract(object):

     def save_model(self, request, obj, form, change):

        obj.author = request.user

        obj.save()


class BaseAdmin(BaseAdminAbstract, admin.ModelAdmin):
    pass


class BaseAdminTree(BaseAdminAbstract, MPTTModelAdmin):
    pass


class PageAdmin(BaseAdminTree):

    fieldsets = [
        (None, {'fields':  ['parent', 'title', 'slug', 'active', 'text', 'sort', 'comments', 'tpl']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    list_display = ('title', 'id', 'slug', 'active', 'sort', 'public_link')

    list_filter = ('active',)

    search_fields = ('id', 'title', 'slug',)

    list_editable = ('sort',)

    def public_link(self, obj):
        url = obj.get_absolute_url()
        return '<a target="_blank" href="%s">%s</a>' % (url, url)

    public_link.allow_tags = True

    public_link.short_description = 'Url'

admin.site.register(Page, PageAdmin)


class IncludeAreaAdmin(BaseAdmin):

    fields = ['title', 'slug', 'active', 'text']

    list_display = ('title', 'slug', 'active')

    list_filter = ('active',)

    search_fields = ('id', 'title', 'slug',)

admin.site.register(IncludeArea, IncludeAreaAdmin)


class MenuAdmin(BaseAdminTree):

    fields = ['parent', 'active', 'title', 'link', 'slug', 'target', 'cls', 'sort']

    list_display = ('title', 'id', 'link', 'active', 'sort')

    list_filter = ('active',)

    search_fields = ('id', 'title', 'slug',)

    list_editable = ('sort',)

admin.site.register(Menu, MenuAdmin)


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'image': AdminImageWidget,
        }


class PhotoInline(admin.TabularInline):

    exclude = ['author']

    model = Photo

    extra = 3

    form = PhotoForm

    ordering = ('sort',)


class PhotoAlbumAdmin(BaseAdmin):

    fields = ['title', 'slug', 'active', 'text']

    list_display = ('title', 'id', 'slug', 'active')

    inlines = [PhotoInline]

    list_filter = ('active',)

    search_fields = ('id', 'title', 'slug',)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.author = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(PhotoAlbum, PhotoAlbumAdmin)


class AppUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (_(u'Additional'), {'fields': ('phone', 'image',)}),
    )

admin.site.register(AppUser, AppUserAdmin)


class PageCommentAdmin(BaseAdminTree):

    exclude = ('author',)

    list_display = ('id', 'username', 'email', 'text', 'page_obj',)

    search_fields = ('id', 'username', 'email',)

    def page_obj(self, comment):
        return '<a href="%s">%s</a>' % (comment.obj.get_absolute_url(), comment.obj.title)

    page_obj.allow_tags = True
    page_obj.short_description = _('Page')

admin.site.register(PageComment, PageCommentAdmin)


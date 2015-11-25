from django import forms
from django.contrib import admin
from django.forms import ModelForm
from midnight_main.admin import BaseAdmin, BaseAdminTree
from midnight_main.widgets import AdminImageWidget
from .models import *


class SectionForm(ModelForm):

    class Meta:
        model = Section
        fields = '__all__'
        widgets = {
            'image': AdminImageWidget,
        }


class SectionAdmin(BaseAdminTree):

    fieldsets = [
        (None, {'fields':  ['parent', 'active', 'title', 'slug', 'sort', 'image', 'annotation', 'text']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    prepopulated_fields = {"slug": ("title",)}

    list_display = ('title', 'id', 'slug', 'active', 'sort', 'public_link')

    list_editable = ('sort', )

    form = SectionForm

    search_fields = ('id', 'title', 'slug',)

    def public_link(self, obj):
        url = obj.get_absolute_url()
        return '<a target="_blank" href="%s">%s</a>' % (url, url)

    public_link.allow_tags = True

    public_link.short_description = 'Url'

admin.site.register(Section, SectionAdmin)


class ParamInline(admin.StackedInline):

    exclude = ['author']

    model = Param

    extra = 3

    ordering = ('sort',)


class ParamGroupAdmin(BaseAdmin):

    exclude = ('author',)

    inlines = (ParamInline,)

admin.site.register(ParamGroup, ParamGroupAdmin)


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'image': AdminImageWidget,
        }


class ParamValueInlineFormSet(forms.models.BaseInlineFormSet):

    model = ParamValue

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial_group = self.request.GET.get('initial_group', None)
        if initial_group:
            group = ParamGroup.objects.get(id=initial_group)
            if not group:
                return
            params = group.param_set.all()
            self.initial = []
            for param in params:
                self.initial.append({'param': param})


class ParamValueInline(admin.StackedInline):

    exclude = ('author',)

    model = ParamValue

    formset = ParamValueInlineFormSet

    extra = 3

    ordering = ('sort',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request
        return formset

    def get_extra(self, request, obj=None, **kwargs):
        extra = super().get_extra(request, obj, **kwargs)
        initial_group = request.GET.get('initial_group', None)
        if initial_group:
            group = ParamGroup.objects.get(id=initial_group)
            if not group:
                return extra
            extra = group.param_set.count()
        return extra


class ProductPhotoInline(admin.StackedInline):

    exclude = ['author']

    model = ProductPhoto

    extra = 3

    ordering = ('sort',)


class ProductAdmin(BaseAdmin):

    fieldsets = [
        (None, {'fields':  ['active', 'title', 'slug', 'sections', 'image', 'price', 'sort', 'annotation', 'text']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    inlines = [ProductPhotoInline, ParamValueInline]

    prepopulated_fields = {"slug": ("title",)}

    list_display = ('title', 'id', 'slug', 'active', 'price', 'public_link')

    list_filter = ('sections', 'active')

    search_fields = ('id', 'title', 'slug',)

    form = ProductForm

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('sections')

    def public_link(self, obj):
        url = obj.get_absolute_url()
        return '<a target="_blank" href="%s">%s</a>' % (url, url)

    public_link.allow_tags = True

    public_link.short_description = 'Url'

    change_list_template = 'admin/product_change_list.html'

    def changelist_view(self, request, extra_context=None):
        resp = super().changelist_view(request, extra_context)
        resp.context_data['param_groups'] = ParamGroup.objects.all()
        return resp

admin.site.register(Product, ProductAdmin)


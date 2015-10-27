from django.contrib import admin
from django.forms import ModelForm
from midnight.base_models import BaseAdmin, BaseAdminTree
from news.models import Section, News
from midnight.widgets import AdminImageWidget

class SectionAdmin(BaseAdminTree):

    fieldsets = [
        (None, {'fields':  ['parent', 'active', 'title', 'slug', 'sort']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    list_display = ('title', 'id', 'slug', 'active', 'sort')

    list_editable = ('sort', )

    search_fields = ('id', 'title', 'slug',)

admin.site.register(Section, SectionAdmin)


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'image': AdminImageWidget,
        }


class NewsAdmin(BaseAdmin):

    fieldsets = [
        (None, {'fields':  ['active', 'title', 'slug', 'date', 'sections', 'image', 'annotation', 'text']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    list_display = ('title', 'id', 'slug', 'active', 'date')

    list_filter = ('sections', 'active')

    search_fields = ('id', 'title', 'slug',)

    form = NewsForm

admin.site.register(News, NewsAdmin)

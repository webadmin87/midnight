from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from midnight.base_models import BaseAdmin, BaseAdminTree
from news.models import Section, News
from midnight.widgets import AdminImageWidget


class SectionAdmin(BaseAdminTree):

    fieldsets = [
        (None, {'fields':  ['parent', 'active', 'title', 'slug', 'sort']}),
        ('SEO', {'fields':  ['metatitle', 'keywords', 'description']}),
    ]

    list_display = ('title', 'id', 'slug', 'active', 'sort', 'public_link')

    list_editable = ('sort', )

    search_fields = ('id', 'title', 'slug',)

    def public_link(self, obj):
        url=reverse('news:news_list', args=[obj.slug])
        return '<a target="_blank" href="%s">%s</a>' % (url, url)

    public_link.allow_tags = True

    public_link.short_description = 'Url'

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

    list_display = ('title', 'id', 'slug', 'active', 'date', 'public_link')

    list_filter = ('sections', 'active')

    search_fields = ('id', 'title', 'slug',)

    form = NewsForm

    def public_link(self, obj):
        url=reverse('news:news_detail', args=[obj.slug])
        return '<a target="_blank" href="%s">%s</a>' % (url, url)

    public_link.allow_tags = True

    public_link.short_description = 'Url'

admin.site.register(News, NewsAdmin)

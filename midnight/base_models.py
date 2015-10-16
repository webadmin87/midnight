from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import MPTTModelAdmin


class Base(models.Model):

    active = models.BooleanField(default=True, verbose_name=_(u'Active'))

    author = models.ForeignKey(User, verbose_name=_(u'Author'))

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class BaseTree(MPTTModel):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name=_(u'Parent'))

    active = models.BooleanField(default=True, verbose_name=_(u'Active'))

    author = models.ForeignKey(User, verbose_name=_(u'Author'))

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def has_childs(self):
        count = self.children.count()
        return count > 0

    class Meta:
        abstract = True


class BaseAdminAbstract(object):

     def save_model(self, request, obj, form, change):

        obj.author = request.user

        obj.save()


class BaseAdmin(BaseAdminAbstract, admin.ModelAdmin):
    pass


class BaseAdminTree(BaseAdminAbstract, MPTTModelAdmin):
    pass


def published(self):
    return self.filter(active=True)

models.QuerySet.published = published

models.Manager.published = published


from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Base(models.Model):
	active = models.BooleanField()
	author = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True
		
class BaseAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()
		


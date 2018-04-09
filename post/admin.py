from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ['category', 'title', 'price', 'user']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
from django.contrib import admin
from .models import Blog, Category, Tag

# Register your models here.

# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ('title',)
    date_hierarchy = 'created_at'

admin.site.register(Blog, BlogAdmin)
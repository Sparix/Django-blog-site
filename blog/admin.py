from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'slug', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


admin.site.register(Car, CarAdmin)
admin.site.register(Categories, CategoryAdmin)

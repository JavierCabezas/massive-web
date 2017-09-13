from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = [
        'name',
        'parent_category',
        'level',
    ]

    list_filter = [
        'parent_category'
    ]

admin.site.register(Category, CategoryAdmin)

from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]

    list_display = [
        '__str__',
        'admin_image',
        'description',
    ]

admin.site.register(Author, AuthorAdmin)

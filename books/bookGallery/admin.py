from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'amount', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'status')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'date')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
    list_display_links = ('id', 'status_name')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dateBirth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone')


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Status, StatusAdmin)

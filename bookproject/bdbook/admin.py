from django.contrib import admin
from .models import Book, BookNumber, Character, Author
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'number']  # mostra só esses dois campos
    list_filter = ['desc']  # mostra um filtro desse campo
    search_fields = ['title']  # faz uma busca por esse campo


@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
    list_display = ['isbn_10', 'isbn_13']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

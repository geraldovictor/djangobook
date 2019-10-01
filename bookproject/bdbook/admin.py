from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price'] #mostra só esses dois campos
    list_filter = ['desc'] #mostra um filtro desse campo
    search_fields = ['title'] #faz uma busca por esse campo
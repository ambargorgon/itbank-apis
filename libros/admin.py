from django.contrib import admin
from .models import Libro
# Register your models here.

class LibroAdmin (admin.ModelAdmin):
    readonly_fields= ('created-at','updated-at')
admin.site.register(Libro)
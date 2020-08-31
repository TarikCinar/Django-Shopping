from django.contrib import admin
from .models import Filtrele


class AdminFiltrele(admin.ModelAdmin):
    list_display = ['filtreleme_turu']

admin.site.register(Filtrele,AdminFiltrele)

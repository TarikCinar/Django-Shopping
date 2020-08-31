from django.contrib import admin
from .models import *
# Register your models here.

class AdminUrunler(admin.ModelAdmin):
    list_display = ['name','price','upload_date','seller']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']

class AdminAltCategory(admin.ModelAdmin):
    list_display = ['alt_category_name']

admin.site.register(Urunler,AdminUrunler)
admin.site.register(Category,AdminCategory)
admin.site.register(AltCategory,AdminAltCategory)
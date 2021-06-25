from django.contrib import admin

from . import models

class CevapInlineModel(admin.TabularInline):
    model = models.CevapModel
    fields = [
        'cevap',
        'dogruMu'
    ]

@admin.register(models.KategoriModel)
class KategoriAdmin(admin.ModelAdmin):
    fields = ['isim']

@admin.register(models.SoruModel)
class SoruAdmin(admin.ModelAdmin):
    fields = [
        'baslik',
        'kategori',
    ]
    list_display = [
        'baslik',
        'kategori'
    ]
    inlines = [
        CevapInlineModel,
    ]

@admin.register(models.CevapModel)
class CevapAdmin(admin.ModelAdmin):
    list_display = [
        'cevap',
        'dogruMu',
        'soru'
    ]

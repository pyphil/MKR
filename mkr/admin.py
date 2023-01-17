from django.contrib import admin
from .models import Kompetenzkarte, Fach


class KompetenzkarteCustomAdmin(admin.ModelAdmin):
    list_display = (
        'kategorie', 'fach', 'jgst', 'vorhaben', 'info', 'medienkompetenz',
        'technik', 'alle_teil', 'pflicht_empf', 'durchf_planung',
        )
    list_filter = (
        'kategorie', 'fach', 'jgst', 'vorhaben', 'info', 'medienkompetenz',
        'technik', 'alle_teil', 'pflicht_empf', 'durchf_planung',
        )


class FachCustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'fach')
    ordering = ['fach']


admin.site.register(Kompetenzkarte, KompetenzkarteCustomAdmin)
admin.site.register(Fach, FachCustomAdmin)

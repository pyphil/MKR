from django.contrib import admin
from .models import Kompetenzkarte, Fach


class KompetenzkarteCustomAdmin(admin.ModelAdmin):
    list_display = (
            'kategorie', 'fach', 'jgst', 'vorhaben', 'info', 'medien'
        )
    list_filter = (
        'kategorie', 'fach', 'jgst', 'vorhaben', 'info', 'medien'
        )


admin.site.register(Kompetenzkarte)
admin.site.register(Fach)

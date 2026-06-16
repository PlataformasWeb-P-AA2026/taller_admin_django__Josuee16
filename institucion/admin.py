from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

class MuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "año_fundacion", "display_costo_total", "display_guias_experiencia")
    search_fields = ("nombre", "ciudad")

    def display_costo_total(self, obj):
        return f"${obj.get_costo_total_produccion():,.2f}"
    display_costo_total.short_description = "Costo Total"

    def display_guias_experiencia(self, obj):
        return obj.get_guias_mas_experiencia()
    display_guias_experiencia.short_description = "Guía Más Experimentado"


class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "museo", "años_experiencia_guia")
    search_fields = ("nombre_completo", "museo__nombre")

class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ("titulo_exhibicion", "guia", "duracion_meses", "costo_produccion", "tematica")
    search_fields = ("titulo_exhibicion", "guia__nombre_completo")


admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo, GuiaMuseoAdmin)
admin.site.register(Exhibicion, ExhibicionAdmin)

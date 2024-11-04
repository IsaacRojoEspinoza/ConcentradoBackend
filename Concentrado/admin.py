from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Avance, Nivel, Entidad, Periodo
from .resources import AvanceResource, NivelResource, EntidadResource, PeriodoResource

class AvanceAdmin(ImportExportModelAdmin):
    resource_class = AvanceResource
    search_fields = ['entidad__nombre_entidad']  # Asegúrate de que el nombre de campo es correcto
    list_filter = ['distrito']
    list_display = ('id','entidad', 'distrito', 'numero_designados', 'numero_inscritos')

    def get_search_results(self, request, queryset, search_term):
        search_term = search_term.strip()
        if search_term:
            queryset = queryset.filter(
                entidad__nombre_entidad__icontains=search_term
            )
        return queryset, False

class NivelAdmin(ImportExportModelAdmin):
    resource_class = NivelResource
    search_fields = ['entidad__nombre_entidad']
    list_display = ('id','entidad', 'nivel_esperado', 'nivel_obtenido')

class EntidadAdmin(ImportExportModelAdmin):
    resource_class = EntidadResource
    search_fields = ['nombre_entidad']
    list_display = ('numero','nombre_entidad', 'logo')

class PeriodoAdmin(ImportExportModelAdmin):
    resource_class = PeriodoResource
    search_fields = ['anio_inicio', 'anio_fin']
    list_display = ('id','anio_inicio', 'anio_fin')

# Registrar los modelos en el panel de administración
admin.site.register(Avance, AvanceAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Entidad, EntidadAdmin)
admin.site.register(Periodo, PeriodoAdmin)

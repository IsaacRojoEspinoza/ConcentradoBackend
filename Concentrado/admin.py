from django.contrib import admin
from .models import Task, Avance
from .resources import AvanceResource
from import_export.admin import ImportExportModelAdmin

# Registrar el modelo Task en el panel de administración
admin.site.register(Task)

class AvanceAdmin(ImportExportModelAdmin):
    resource_class = AvanceResource
    search_fields = ['entidad', 'nombreEntidad']
    list_filter = ['distrito']
    list_display = ('entidad', 'nombreEntidad', 'distrito')

    def get_search_results(self, request, queryset, search_term):
        search_term = search_term.strip()
        if search_term:
            queryset = queryset.filter(
                entidad__iexact=search_term
            ) | queryset.filter(
                nombreEntidad__iexact=search_term
            )
        return queryset, False  # El segundo valor False indica que no se han realizado correcciones de búsqueda.

    def get_search_fields(self, request):
        return self.search_fields

# Registrar el modelo Avance en el panel de administración con la funcionalidad personalizada
admin.site.register(Avance, AvanceAdmin)

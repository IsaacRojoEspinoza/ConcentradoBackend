from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Avance,Año,Entidad
from .resources import AvanceResource  # Asegúrate de que el recurso esté importado correctamente
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class AvanceAdmin(ImportExportModelAdmin):
    resource_class = AvanceResource
    search_fields = ['entidad', 'nombreEntidad']
    list_filter = ['distrito']
    list_display = ('entidad', 'nombreEntidad', 'distrito')

    def get_search_results(self, request, queryset, search_term):
        search_term = search_term.strip()
        if search_term:
            queryset = queryset.filter(
                entidad__icontains=search_term
            ) | queryset.filter(
                nombreEntidad__icontains=search_term
            )
        # No se realiza ningún filtrado adicional si no hay término de búsqueda
        return queryset, False  # El segundo valor False indica que no se han realizado correcciones de búsqueda.

    def get_search_fields(self, request):
        return self.search_fields
    
class AñoResource(resources.ModelResource):
    class Meta:
        model = Año
        fields = ('año',)

class EntidadResource(resources.ModelResource):
    class Meta:
        model = Entidad
        fields = ('numero', 'nombreEntidad', 'numeroDeDistritos', 'logo_url', 'años')
        import_id_fields = ('numero',)

    def before_import_row(self, row, **kwargs):
        # Ensure 'años' field is a string, then process it
        años_field = row.get('años', '')
        if isinstance(años_field, str):
            años_ids = [int(año_id.strip()) for año_id in años_field.split(';') if año_id.strip().isdigit()]
            row['años'] = años_ids
        return super().before_import_row(row, **kwargs)

    def import_obj(self, obj, **kwargs):
        # Retrieve years IDs from kwargs
        años_ids = kwargs.get('años', [])
        if años_ids:
            obj.save()  # Save the object first
            obj.años.set(años_ids)  # Set the ManyToMany relationship
        else:
            obj.save()
        return obj

# Configura el admin para Año
@admin.register(Año)
class AñoAdmin(ImportExportModelAdmin):
    resource_class = AñoResource

# Configura el admin para Entidad
@admin.register(Entidad)
class EntidadAdmin(ImportExportModelAdmin):
    resource_class = EntidadResource

    
admin.site.register(Avance, AvanceAdmin)

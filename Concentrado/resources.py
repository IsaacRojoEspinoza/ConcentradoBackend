from import_export import resources
from .models import Avance, Nivel, Entidad, Periodo

class AvanceResource(resources.ModelResource):
    class Meta:
        model = Avance
        fields = ('id', 'entidad', 'distrito', 'numeroDesignados', 'numeroInscritos', 
                  'inscritosDesignados', 'conIngreso', 'conIngresoInscritos', 
                  'sinIngreso', 'sinIngresoInscritos', 'concluyeron', 
                  'concluyeronDesignados')  # Incluye 'id' si lo necesitas
        import_id_fields = ('id',)  # Especifica qué campo usar para la importación

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

class NivelResource(resources.ModelResource):
    class Meta:
        model = Nivel
        fields = ('id', 'entidad', 'nivelEsperado', 'nivelObtenido')  # Ajusta según tus campos
        import_id_fields = ('id',)

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

class EntidadResource(resources.ModelResource):
    class Meta:
        model = Entidad
        fields = ('numero', 'nombreEntidad', 'numeroDeDistritos', 'logo')  # Ajusta según tus campos
        import_id_fields = ('numero',)

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

class PeriodoResource(resources.ModelResource):
    class Meta:
        model = Periodo
        fields = ('id', 'anio_inicio', 'anio_fin')  # Ajusta según tus campos
        import_id_fields = ('id',)

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

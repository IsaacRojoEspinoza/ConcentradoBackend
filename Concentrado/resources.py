from import_export import resources
from import_export.fields import Field
from .models import Avance, Nivel, Entidad, Periodo

class AvanceResource(resources.ModelResource):
    class Meta:
        model = Avance
        fields = ('id','entidad', 'distrito', 'numero_designados', 'numero_inscritos', 
                  'inscritos_designados', 'con_ingreso', 'con_ingreso_inscritos', 
                  'sin_ingreso', 'sin_ingreso_inscritos', 'concluyeron', 
                  'concluyeron_designados','periodo')  # Incluye 'id' si lo necesitas
        import_id_fields = ('id',)  # Especifica qué campo usar para la importación

def import_row(self, row, instance=None, **kwargs):
    # Obtener el valor para 'entidad'
    entidad_id = row.get('entidad')
    if entidad_id:
        try:
            entidad_id = int(entidad_id)  # Asegúrate de que sea un entero
            entidad_instance = Entidad.objects.get(id=entidad_id)
            row['entidad'] = entidad_instance.id  # Asegúrate de que este sea el ID
        except ValueError:
            raise ValueError(f"ID de entidad '{entidad_id}' no es un número válido.")
        except Entidad.DoesNotExist:
            raise ValueError(f"Entidad con ID '{entidad_id}' no encontrada.")
    
    # Obtener el valor para 'periodo'
    periodo_id = row.get('periodo')
    if periodo_id:
        try:
            periodo_id = int(periodo_id)  # Asegúrate de que sea un entero
            periodo_instance = Periodo.objects.get(id=periodo_id)
            row['periodo'] = periodo_instance.id  # Asegúrate de que este sea el ID
        except ValueError:
            raise ValueError(f"ID de periodo '{periodo_id}' no es un número válido.")
        except Periodo.DoesNotExist:
            raise ValueError(f"Periodo con ID '{periodo_id}' no encontrado.")

    return super().import_row(row, instance, **kwargs)
class NivelResource(resources.ModelResource):
    class Meta:
        model = Nivel
        fields = ('entidad', 'nivel_esperado', 'nivel_obtenido', 'periodo')
        import_id_fields = ('entidad',)

def import_row(self, row, instance=None, **kwargs):
    # Obtener el valor para 'entidad'
    entidad_id = row.get('entidad')
    if entidad_id:
        try:
            entidad_id = int(entidad_id)  # Asegúrate de que sea un entero
            entidad_instance = Entidad.objects.get(id=entidad_id)
            row['entidad'] = entidad_instance.id  # Asegúrate de que este sea el ID
        except ValueError:
            raise ValueError(f"ID de entidad '{entidad_id}' no es un número válido.")
        except Entidad.DoesNotExist:
            raise ValueError(f"Entidad con ID '{entidad_id}' no encontrada.")
    
    # Obtener el valor para 'periodo'
    periodo_id = row.get('periodo')
    if periodo_id:
        try:
            periodo_id = int(periodo_id)  # Asegúrate de que sea un entero
            periodo_instance = Periodo.objects.get(id=periodo_id)
            row['periodo'] = periodo_instance.id  # Asegúrate de que este sea el ID
        except ValueError:
            raise ValueError(f"ID de periodo '{periodo_id}' no es un número válido.")
        except Periodo.DoesNotExist:
            raise ValueError(f"Periodo con ID '{periodo_id}' no encontrado.")

    return super().import_row(row, instance, **kwargs)

class EntidadResource(resources.ModelResource):
    class Meta:
        model = Entidad
        fields = ('numero', 'nombre_entidad', 'logo')  # Ajusta según tus campos
        import_id_fields = ('numero','nombre_entidad','logo')

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

class PeriodoResource(resources.ModelResource):
    class Meta:
        model = Periodo
        fields = ('id', 'anio_inicio', 'anio_fin')  # Ajusta según tus campos
        import_id_fields = ('id',)

    def import_row(self, row, *args, **kwargs):
        return super().import_row(row, *args, **kwargs)

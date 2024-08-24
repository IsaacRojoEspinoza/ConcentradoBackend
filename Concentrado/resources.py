from import_export import resources
from .models import Avance  # Asegúrate de usar el nombre correcto del modelo

class AvanceResource(resources.ModelResource):
    class Meta:
        model = Avance
        fields = ('entidad','nombreEntidad','distrito','numeroDesignados','numeroInscritos','inscritosDesignados','conIngreso','conIngresoInscritos','sinIngreso','sinIngresoInscritos','concluyeron','concluyeronDesignados')
        import_id_fields = ()  # No importa el campo 'id'

    def import_row(self, row, *args, **kwargs):
        # Llama al método base si no necesitas modificar la fila
        return super().import_row(row, *args, **kwargs)
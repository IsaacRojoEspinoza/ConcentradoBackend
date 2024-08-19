from django.contrib import admin
from .models import Task
from .models import Avance
from .models import Avance  # Asegúrate de usar el nombre correcto del modelo
from .resources import AvanceResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Task)

class AvanceAdmin(ImportExportModelAdmin):
    resource_class = AvanceResource

admin.site.register(Avance, AvanceAdmin)
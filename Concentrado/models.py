from django.db import models
 
class Avance(models.Model):
    entidad = models.IntegerField() 
    nombreEntidad = models.CharField(max_length=255)
    distrito = models.IntegerField()
    numeroDesignados = models.IntegerField()
    numeroInscritos = models.IntegerField()
    inscritosDesignados = models.DecimalField(max_digits=5, decimal_places=2)
    conIngreso = models.IntegerField()
    conIngresoInscritos = models.DecimalField(max_digits=5, decimal_places=2)
    sinIngreso = models.IntegerField()
    sinIngresoInscritos = models.DecimalField(max_digits=5, decimal_places=2)
    concluyeron = models.IntegerField()
    concluyeronDesignados = models.DecimalField(max_digits=5, decimal_places=2)
    # fee = models.IntegerField()

# requiero que los campos de este modelo sean visibles en el adminpanel de django y que se puedan importar y exportar ya tengo instalada esta dependendencia django-import-export==4.1.1
class Año(models.Model):
    año = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.año)

class Entidad(models.Model):
    numero = models.IntegerField(primary_key=True)
    nombreEntidad = models.CharField(max_length=255)
    numeroDeDistritos = models.IntegerField()
    logo_url = models.CharField(max_length=255)
    años = models.ManyToManyField('Año', blank=True)

    def __str__(self):
        return self.nombreEntidad
    
class Nivel(models.Model):
    numeroEntidad= models.IntegerField(primary_key=True)
    nivelEsperado= models.DecimalField(max_digits=5, decimal_places=2)
    nivelObtenido= models.DecimalField(max_digits=5, decimal_places=2)
    
    # fee = models.IntegerField()
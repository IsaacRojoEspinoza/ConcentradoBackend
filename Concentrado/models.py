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

class Entidad(models.Model):
    numero= models.IntegerField(primary_key=True)
    nombreEntidad = models.CharField(max_length=255)
    numeroDeDistritos = models.IntegerField()
    Logo = models.FileField(upload_to='public/assets')
    # fee = models.IntegerField()
    
class Nivel(models.Model):
    numeroEntidad= models.IntegerField(primary_key=True)
    nivelEsperado= models.DecimalField(max_digits=5, decimal_places=2)
    nivelOptenido= models.DecimalField(max_digits=5, decimal_places=2)
    
    # fee = models.IntegerField()
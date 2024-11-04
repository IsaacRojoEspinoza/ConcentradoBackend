from django.db import models

class Periodo(models.Model):
    anio_inicio = models.PositiveIntegerField()
    anio_fin = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.anio_inicio}-{self.anio_fin}"

class Entidad(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre_entidad = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, default='public/assets/')

    def __str__(self):
        return self.nombre_entidad

class Avance(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='avances')
    distrito = models.IntegerField()
    numero_designados = models.IntegerField()
    numero_inscritos = models.IntegerField()
    inscritos_designados = models.DecimalField(max_digits=5, decimal_places=2)
    con_ingreso = models.IntegerField()
    con_ingreso_inscritos = models.DecimalField(max_digits=5, decimal_places=2)
    sin_ingreso = models.IntegerField()
    sin_ingreso_inscritos = models.DecimalField(max_digits=5, decimal_places=2)
    concluyeron = models.IntegerField()
    concluyeron_designados = models.DecimalField(max_digits=5, decimal_places=2)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='avances')

    def __str__(self):
        return f"Avance de {self.entidad.nombre_entidad} en distrito {self.distrito}"

class Nivel(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='niveles')
    nivel_esperado = models.DecimalField(max_digits=5, decimal_places=2)
    nivel_obtenido = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='niveles')

    def __str__(self):
        return f"Nivel de {self.entidad.nombre_entidad}"


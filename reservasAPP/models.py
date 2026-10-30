from django.db import models

# Create your models here.

class Estado(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado
    

class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre


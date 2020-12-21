from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg


class User(AbstractUser):
    def __str__(self):
        return self.username


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.tipo + " Precio: " + str(self.precio) + "€"


class Cita(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    import pytz as tz
    import datetime as dt
    fecha = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return (
            "Cliente: "
            + str(self.cliente)
            + " Empleado: "
            + str(self.empleado)
            + " Servicio: "
            + str(self.servicio)
            + " Fecha: "
            + str(self.fecha)
        )

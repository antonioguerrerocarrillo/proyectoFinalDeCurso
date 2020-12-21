from django.contrib import admin
from .models import User, Empleado, Cita, Servicio

# Register your models here.
admin.site.register(User)
admin.site.register(Empleado)
admin.site.register(Cita)
admin.site.register(Servicio)
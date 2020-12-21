from rest_framework import serializers

from .models import User, Empleado, Servicio, Cita


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ("id", "nombre")


class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = ("id", "tipo", "precio")


class CitaSerializer(serializers.HyperlinkedModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True, default=None
    )
    empleado = serializers.PrimaryKeyRelatedField(
        queryset=Empleado.objects.all(), required=False, allow_null=True, default=None
    )
    servicio = serializers.PrimaryKeyRelatedField(
        queryset=Servicio.objects.all(), required=False, allow_null=True, default=None
    )


    class Meta:
        model = Cita
        fields = ("id", "cliente", "empleado", "servicio", "fecha")

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from datetime import datetime
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

class EmpleadoViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        return Empleado.objects.all()

class ServicioViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.all()


class CitaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def get_queryset(self):
        return Cita.objects.filter(cliente=self.request.user.pk)

    def perform_create(self, serializer):
        post = self.request.data
        cliente = self.request.user
        empleado = post['empleado']
        servicio = post['servicio']
        serializer.save(cliente=cliente)

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"empleado", views.EmpleadoViewSet)
router.register(r"servicio", views.ServicioViewSet)
router.register(r"cita", views.CitaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]
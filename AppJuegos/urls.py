
from django.urls import path
from AppJuegos.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("juegosdecartas/", juegosdecartas, name="juegosdecartas"),
    path("juegosdemesa/", juegosdemesa, name="juegosdemesa"),
    path("busquedaCartas/", busquedaCartas, name="busquedaCartas"),
    path("videoJuegos/", videoJuegos, name="videoJuegos"),
    path("buscar/", buscar, name="buscar"),
]
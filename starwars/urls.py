from django.urls import path
from . import views
from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework import routers
from starwars.views import PersonajeViewSet, PlanetaViewSet, PeliculaViewSet

router = routers.DefaultRouter()

router.register(r"personajes", PersonajeViewSet)
router.register(r"planetas",   PlanetaViewSet)
router.register(r"peliculas",  PeliculaViewSet)

# URLConf
urlpatterns = [
    path("", include(router.urls))
]
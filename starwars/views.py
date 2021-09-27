from rest_framework import filters
from rest_framework import VERSION, viewsets, status

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response

from starwars.serializers import PersonajeSerializer, PlanetaSerializer, PeliculaSerializer
from starwars.models import Personaje, Planeta, Pelicula
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@permission_classes([IsAuthenticated])
class PersonajeViewSet(viewsets.ModelViewSet):
    
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre','genero']

    def retrieve(self, request, *args, **kwargs):
        
        return super(PersonajeViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        
        return super(PersonajeViewSet, self).list(request, *args, **kwargs)
@permission_classes([IsAuthenticated])
class PlanetaViewSet(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']
    
    def retrieve(self, request, *args, **kwargs):
        return super(PlanetaViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PlanetaViewSet, self).list(request, *args, **kwargs)
@permission_classes([IsAuthenticated])
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
    
    def retrieve(self, request, *args, **kwargs):
        return super(PeliculaViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PeliculaViewSet, self).list(request, *args, **kwargs)


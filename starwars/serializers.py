from rest_framework import serializers
from starwars.models import Personaje, Pelicula, Planeta

class PersonajeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Personaje
        fields = (
            "nombre",
            "genero",
            "altura",
            "creado",
            "editado",
            "url",
            "peliculas",
            "img",
        )

class PlanetaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Planeta
        fields = (
            "nombre",
            "diametro",
            "periodo_rotacion",
            "periodo_orbitacion",
            "poblacion",
            "creado",
            "editado",
            "url",
            "img",
        )

class PeliculaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pelicula
        fields = (            
            "titulo",
            "director",
            "productor",
            "texto_intro",
	        "fecha",
            "personajes",
            "planetas",
            "creado",
            "editado",
            "url",
            "img",
            "pelicula_id",
        )
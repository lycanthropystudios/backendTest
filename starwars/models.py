from django.db import models
from django.db.models.base import Model, ModelState
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token;
from django.contrib.auth.models import User
# Create your models here.
class Crear(models.Model):
    class Meta:
        abstract = True
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
class Personaje(Crear):
    nombre = models.CharField(max_length=120)
    genero = models.CharField(max_length=50, blank=True)
    altura = models.CharField(max_length=10, blank=True)
    img = models.CharField(max_length=500, blank=True)

class Planeta(Crear):
    nombre = models.CharField(max_length=100)
    diametro = models.CharField(max_length=50)
    periodo_rotacion = models.CharField(max_length=50)
    periodo_orbitacion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    img = models.CharField(max_length=500, blank=True)

class Pelicula(Crear):
    titulo = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    productor = models.CharField(max_length=120)
    texto_intro = models.CharField(max_length=800)
    fecha = models.DateField()
    img = models.CharField(max_length=500, blank=True)
    pelicula_id = models.IntegerField()
    
    personajes = models.ManyToManyField(
        Personaje,
        related_name="peliculas",
        blank=True
    )

    planetas = models.ManyToManyField(
        Planeta,
        related_name="peliculas",
        blank=True
    )
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

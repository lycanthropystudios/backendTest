from django.contrib import admin

# Register your models here.
from .models import (
    Personaje,
    Planeta,
    Pelicula

)

classes = [Personaje, Planeta, Pelicula]

for c in classes:
    admin.site.register(c)
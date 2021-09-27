from __future__ import unicode_literals
from starwars import admin
from django.contrib.auth.models import User
from django.http import response

from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from .models import Personaje, Pelicula, Planeta
import json

class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test@321")
        
    def test_endpoint_personajes(self):
        self.client.force_login(self.user)    
        response = self.client.get("http://localhost:8000/personajes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_endpoint_peliculas(self):
        self.client.force_login(self.user)    
        response = self.client.get("http://localhost:8000/peliculas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_endpoint_planetas(self):
        self.client.force_login(self.user)    
        response = self.client.get("http://localhost:8000/planetas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        data = {"username":"admin", "password":"admin"}
        response = self.client.post("http://localhost:8000/auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_perfil_no_autenticado_busca_info(self):        
        response = self.client.get("http://localhost:8000/personajes/?search=Luke")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_perfil_autenticado_busca_info(self):
        data = {"username":"admin", "password":"admin"}        
        response = self.client.get("http://localhost:8000/auth/login/?next=/personajes/?search=Luke", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_crear_personajes(self):
        self.client.force_login(self.user)    
        data = {"editado": "2021-12-20T21:17:56.891Z",
            "nombre": "Makai",
            "creado": "2021-09-09T13:50:51.644Z",
            "genero": "male",
            "altura": "205",
            "img": ""}
        response = self.client.post("http://localhost:8000/personajes/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_crear_planetas(self):
        self.client.force_login(self.user)    
        data = {"editado": "2011-12-20T20:58:18.411Z",
            "nombre": "Antioquia",
            "diametro": "185489",
            "periodo_rotacion": "68",
            "creado": "2015-12-09T13:50:49.641Z",
            "periodo_orbitacion": "30",
            "poblacion": "900000",
            "img": ""}
        response = self.client.post("http://localhost:8000/planetas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

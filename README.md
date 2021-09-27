# Startwars API
## _Prueba Backend Dev - Gearplug_
> info: Proyecto Django Rest Documentado - johann9616@gmail.com
## Instalacion
```sh
pip install -r requirements.txt
```
## Cargar Informacion del Fixture
```sh
python manage.py loaddata planeta.json
python manage.py loaddata pelicula.json
python manage.py loaddata personaje.json
```
## Build
```sh
python manage.py migrate
python manage.py createsuperuser
```
## Iniciar
```sh
python manage.py runserver
```

## Sitemap
Para _consultar_ y _agregar_ [POST/GET] request en los endpoints de datos se debe iniciar sesión
#### username : admin password : admin

| Endpoint | URL |
| ------ | ------ |
| Home | http://127.0.0.1:8000/ |
| Personajes | http://127.0.0.1:8000/personajes/ |
| Planetas | http://127.0.0.1:8000/planetas/ |
| Peliculas | http://127.0.0.1:8000/peliculas/ |
| Login | http://127.0.0.1:8000/auth/login |
| Admin | http://127.0.0.1:8000/admin/ |
| Documentacion | http://127.0.0.1:8000/docs/ |
| Schema | http://127.0.0.1:8000/schema |

## Capturas - Sin autenticacion
![Image](https://i.imgur.com/Nd1wluw.jpeg)
![Image](https://i.imgur.com/71y25Sf.jpeg)
![Image](https://i.imgur.com/Bc2IeF7.jpeg)
![Image](https://i.imgur.com/aGW3mFG.jpeg)
![Image](https://i.imgur.com/oXLGrUx.jpeg)
## Capturas - Con autenticacion
![Image](https://i.imgur.com/GT9Y0kx.jpeg)
## Filtro de busqueda
![Image](https://i.imgur.com/frZFiIG.jpeg)
## Agregar datos
![Image](https://i.imgur.com/yp6nlPM.jpeg)
## Documentacion
![Image](https://i.imgur.com/ZXVbrRs.jpeg)
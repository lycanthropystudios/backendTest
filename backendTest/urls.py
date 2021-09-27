"""backendTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from backendTest.views import index
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from . import views

urlpatterns = [
    path('', include('starwars.urls')),
    path('admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework.urls', # ADD THIS URL
                               namespace='rest_framework')),
    path('docs/', include_docs_urls(title="Starwars API Doc")),
    path('schema', get_schema_view(
        title="Starwars",
        description="API test",
        version="1.0"),
        name="openapi-schema"
    )
]

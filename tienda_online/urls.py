"""
URL configuration for tienda_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from gest_pedidos.views import busqueda_productos,buscar,exit, alta_usuario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("busqueda_productos/",busqueda_productos),
    path("buscar/",buscar),
    path("accounts/",include('django.contrib.auth.urls')),
    path("logout/",exit),
    path("register/", alta_usuario)
]

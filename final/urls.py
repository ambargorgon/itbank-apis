"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from itbankFs import views
from api.views  import SucursalViewSet

urlpatterns = [
    path('', views.home),
    path('atCliente/', views.atCliente),
    path('prestamos/',views.prestamos),
    path('seguros/', views.seguros),
    path('tarjetas/', views.tarjetas),
    path('dolarHoy/', views.dolarHoy),
    path('calculadora/', views.calculadora),
    path('clientes/', views.clientes),
    path('cuentas/', views.cuentas),
    path('admin/', admin.site.urls),
    path('homebanking/', views.homebanking),
    

    path('', include('api.urls'))

]

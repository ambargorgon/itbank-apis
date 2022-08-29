from django.contrib import admin
from django.urls import path, include
from itbankFs import views

from api.views import SucursalViewSet, ClienteViewSet

urlpatterns = [
    path('',views.home),
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

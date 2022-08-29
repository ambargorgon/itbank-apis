from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Cree un enrutador y registre nuestros conjuntos de vistas con él.
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')
router.register(r'api/clientes', views.ClienteViewSet, basename='cliente')
router.register(r'api/cuentas',  views.CuentaViewSet, basename='cuenta')
router.register(r'api/prestamos',  views.PrestamoViewSet, basename='prestamo')
router.register(r'api/tarjetas',  views.TarjetaViewSet, basename='tarjeta')
router.register(r'api/sucursales',  views.SucursalViewSet, basename='sucursal')

# router.register(r'cliente', views.ClienteViewSet)
# Las URL de la API ahora las determina automáticamente el enrutador.
urlpatterns = [path('', include(router.urls)), ]

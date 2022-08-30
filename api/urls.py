from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Cree un enrutador y registre nuestros conjuntos de vistas con él.
router = DefaultRouter()
router.register(r'api/datos-cliente', views.DatosCliente, basename='datos-cliente')
router.register(r'api/saldo-cliente', views.SaldoCliente, basename='saldo-cliente')
router.register(r'api/prestamo-cliente', views.PrestamoCliente, basename='prestamo-cliente')
router.register(r'api/prestamo-sucursal', views.PrestamoSucursal, basename='prestamo-sucursal')
router.register(r'api/tarjeta-cliente', views.TarjetasDeCliente, basename='tarjeta-cliente')
router.register(r'api/solicitar-prestamo', views.SolicitarPrestamo, basename='solicitar-prestamo')
router.register(r'api/anular-prestamo', views.AnularPrestamo, basename='anular-prestamo')
router.register(r'api/modificar-direccion', views.ModificarDireccion, basename='modificar-direccion')
router.register(r'api/sucursales', views.Sucursales, basename='sucursales')

# router.register(r'api/clientes', views.ClienteViewSet, basename='cliente')
# router.register(r'api/cuentas',  views.CuentaViewSet, basename='cuenta')
# router.register(r'api/prestamos',  views.PrestamoViewSet, basename='prestamo')
# router.register(r'api/tarjetas',  views.TarjetaViewSet, basename='tarjeta')
# router.register(r'api/sucursales',  views.SucursalViewSet, basename='sucursal')

# router.register(r'cliente', views.ClienteViewSet)
# Las URL de la API ahora las determina automáticamente el enrutador.
urlpatterns = [path('', include(router.urls)), ]

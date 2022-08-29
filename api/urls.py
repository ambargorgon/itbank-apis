from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Cree un enrutador y registre nuestros conjuntos de vistas con él.
router = DefaultRouter()
router.register(r'sucursal', views.SucursalViewSet, basename='sucursal')
router.register(r'cliente', views.ClienteViewSet)
# Las URL de la API ahora las determina automáticamente el enrutador.
urlpatterns = [path('', include(router.urls)),]



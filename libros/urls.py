from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libros import views

# Cree un enrutador y registre nuestros conjuntos de vistas con él.
router = DefaultRouter()
router.register(r'libros', views.LibroViewSet)
router.register(r'users', views.UserViewSet)
# Las URL de la API ahora las determina automáticamente el enrutador.
urlpatterns = [path('', include(router.urls)),]
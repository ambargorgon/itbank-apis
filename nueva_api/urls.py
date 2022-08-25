from django.contrib import admin
from django.urls import path
from libros.views import LibroLists
from libros.views import LibroDetails
from libros.views import UserList, UserDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', LibroLists.as_view()),
    path('libros/<int:pk>', LibroDetails.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view())
]
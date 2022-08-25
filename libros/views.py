from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from libros.models import Libro
from libros.serializers import LibroSerializer
from libros.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
class LibroLists(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request, format=None):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ver todos los libros
    def get(self, request): 
        libros = Libro.objects.all().order_by('created_at')
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(libros, request)
        serializer = LibroSerializer(result_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LibroDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        libro = Libro.objects.filter(pk=pk).first()
        serializer = LibroSerializer(libro)
        if libro:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#borrar un libro   
    def delete(self, request, pk):
        libro = Libro.objects.filter(pk=pk).first()
        if libro:
            serializer = LibroSerializer(libro)
            libro.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
#actualizar un libro
    def put(self, request, pk):
        libro = Libro.objects.filter(pk=pk).first()
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#clase para manejar múltiples instancias
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#clase para manejar una única instancia
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'libros': reverse('libros-list', request=request, format=format)
    })
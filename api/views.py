from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Sucursal, Cliente, Cuenta, Prestamo
from .serializers import ClienteSerializer, CuentaSerializer, PrestamoSerializer, SucursalSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from itertools import chain
from rest_framework.decorators import action


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
        
#     def delete(self, request, pk):
#         Sucursal = Sucursal.objects.filter(pk=pk).first()
#         if Sucursal:
#             serializer = SucursalSerializer(Sucursal)
#             Sucursal.delete()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)

# #actualizar un libro
#     def put(self, request, pk):
#         Sucursal = Sucursal.objects.filter(pk=pk).first()
#         serializer = SucursalSerializer(Sucursal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Nueva ViewSet:
class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cliente.objects.all()
    print(queryset)
    serializer_class = ClienteSerializer


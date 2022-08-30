from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from itbankFs.models import Sucursal, Cliente, Cuenta, Prestamo, Tarjeta, TipoCliente
from .serializers import CuentaSerializer, PrestamoSerializer, SucursalSerializer, ClienteSerializer, TarjetaSerializer, UserSerializer, TipoClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

import datetime
from itertools import chain
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

# OBTENER DATOS DE CLIENTE
# 1. Un cliente autenticado, puede obtener sus propios datos
class DatosCliente(viewsets.ReadOnlyModelViewSet):

    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer_id = self.request.user.username
        cliente = Cliente.objects.filter(customer_id=customer_id)
        return cliente

# OBTENER SALDO DE CUENTA DE CLIENTE
# 2. Un cliente autenticado, puede obtener su tipo de cuenta y su saldo
class SaldoCliente(viewsets.ReadOnlyModelViewSet):

    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):

        customer_id = self.request.user.username
        cuenta = Cuenta.objects.filter(customer_id=customer_id)
        # tipoCuenta = TipoClienteSerializer(TipoCliente.objects.filter(customer_id=customer_id), many=True)
        # # get client_type from tipocuenta
        # client_type = tipoCuenta.data[0]['client_type']

        # # convert cuenta query set into list
        # cuenta_list = list(cuenta)
        # # client type list
        # tipoCuenta_list = list(tipoCuenta.data)

        # # get balance from cuenta list
        # # join cuenta list and tipoCuenta list
        # cuenta_tipoCuenta_list = list(chain(cuenta_list, tipoCuenta_list))
        
        return cuenta

        # return cuentas
        # show both cuenta and client_type
        # return cuenta + client_type#chain(cuenta, client_type)

# OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
# 3. Un cliente autenticado, puede obtener el tipo de préstamo y el total del mismo
class PrestamoCliente(viewsets.ReadOnlyModelViewSet):

        serializer_class = PrestamoSerializer
    
        def get_queryset(self):

            prestamo = Prestamo.objects.all().filter(customer_id=self.request.user.username)

            return prestamo

# OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
# 4. Un empleado autenticado puede obtener el listado de prestamos otorgados por una sucursal
class PrestamoSucursal(viewsets.ReadOnlyModelViewSet):

    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):

        sucursal_id = self.request.GET.get('sucursal_id')

        # get all clients from Cliente that have branch
        cliente = Cliente.objects.all().filter(branch=sucursal_id)

        # get all loans from clientes in cliente
        prestamo = Prestamo.objects.all().filter(customer_id__in=cliente)

        return prestamo
    
# OBTENER TARJETAS ASOCIALDAS A UN CLIENTE
# 5. Un empleado autentiacado puede obtener el listado de tarjetas de crédito de un cliente determinado
class TarjetasDeCliente(viewsets.ReadOnlyModelViewSet):

    serializer_class = TipoClienteSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):

        customer_id = self.request.GET.get('customer_id')
        tipo_cuenta = TipoCliente.objects.all().filter(customer_id=customer_id)
        

        return tipo_cuenta

# GENERAR SOLICITUD DE PRÉSTAMO PARA CLIENTE
# 6. Un empleado autenticado puede solicitar un préstamo para un cliente, registrado el mismo y acreditando el saldo en su cuenta
class SolicitarPrestamo(viewsets.ModelViewSet):

    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):

            # if the request has arguments
            if self.request.GET.get('customer_id') and self.request.GET.get('amount'):

            
                customer_id = self.request.GET.get('customer_id')
                loan_amount = self.request.GET.get('loan_amount')
                
                # update balance of customer_id
                cuenta = Cuenta.objects.all().filter(customer_id=customer_id)
                balance = cuenta.values('balance')[0]['balance']
                cuenta.update(balance=int(balance)+int(loan_amount))


# ANULAR SOLICITUD DE PRÉSTAMO DE CLIENTE
# 7. Un empleado autenticado puede anular un préstamo para un cliente, registrado el mismo y revirtiendo el monto correspondiente en su cuenta
class AnularPrestamo(viewsets.ModelViewSet):

    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAdminUser]

    # get customer_id from request.GET
    def get_queryset(self):

        loan_id = self.request.GET.get('loan_id')
        customer_id = self.request.GET.get('customer_id')
        loan_total = self.request.GET.get('loan_total')

        cuenta = Cuenta.objects.all().filter(customer_id=customer_id)
        balance = cuenta.values('balance')[0]['balance']
        cuenta.update(balance=int(balance)-int(loan_total))

        # delete loan from customer_id
        prestamo = Prestamo.objects.all().filter(loan_id=loan_id)
        prestamo.delete()


# MODIFICAR DIRECCION DE CLIENTE
# 8. El propio cliente autenticado o un empleado puede modificar las direcciones
class ModificarDireccion(viewsets.ModelViewSet):

    # only show customer_id and address in url
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # only offer customer_id and address_id to update in request.data
    def get_queryset(self):

        # if user is admin
        if self.request.user.is_superuser:
             customer_id = self.request.GET.get('customer_id')

        elif self.request.user.is_authenticated:
            customer_id = self.request.user.username

        directions = self.request.GET.get('directions')

        # update directions of customer_id
        cliente = Cliente.objects.all().filter(customer_id=customer_id)
        cliente.update(directions=directions)
    
        return cliente

# LISTADO DE TODAS LAS SUCURSALES
# 9. Un endpoint público que devuelve el listado de todas las sucursales con la información correspondiente
class Sucursales(viewsets.ReadOnlyModelViewSet):
    
        serializer_class = SucursalSerializer
    
        def get_queryset(self):
    
            sucursales = Sucursal.objects.all()
    
            return sucursales

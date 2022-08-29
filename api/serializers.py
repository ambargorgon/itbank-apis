from rest_framework import serializers
from dataclasses import fields
from .models import Sucursal, Cliente, Cuenta, Prestamo
from django.contrib.auth.models import User


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    # sucursal = Sucursal.objects.all()
    # sucursales = serializers.PrimaryKeyRelatedField(queryset=sucursal)
    class Meta:
        model = Sucursal
        fields = ['branch_id', 'branch_number', 'branch_name', 'branch_address_id', "direccion"]
        read_only_fields = (
            "customer_id",
        )

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    clientes = serializers.PrimaryKeyRelatedField(many=True, queryset=Cliente.objects.all())
    
    class Meta:
        model = Cliente
        fields = ['customer_id', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch', 'directions']

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    cuentas = serializers.PrimaryKeyRelatedField(many=True, queryset=Cuenta.objects.all())
    
    class Meta:
        model = Cuenta
        fields = ['account_id', 'customer_id', 'balance', 'iban']

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    prestamos = serializers.PrimaryKeyRelatedField(many=True, queryset=Prestamo.objects.all())
    
    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_type', 'loan_date', 'loan_total']
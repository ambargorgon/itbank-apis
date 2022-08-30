from rest_framework import serializers
from itbankFs.models import Sucursal, Cliente, Cuenta, Prestamo, Tarjeta, TipoCliente
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['branch_id', 'branch_number', 'branch_name', 'branch_address_id', 'directions']


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['loan_id', 'loan_type', 'loan_date', 'loan_total', 'customer_id']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        # indicamos que use todos los campos
        fields = ['customer_id', 'customer_name', 'customer_surname',
                  'customer_dni', 'dob', 'branch', 'directions']
        # les decimos cuales son los de solo lectura
        read_only_fields = (
            "customer_id",
        )


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['balance']
        read_only_fields = (
            "account_id",
        )

        


class TarjetaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tarjeta
        fields = ['card_id', 'card_number', 'customer_id', 'cvv',
                  'creation_date', 'expire_date', 'card_type', 'brand','client_type']

class TipoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCliente
        fields = ['customer_id', 'client_type', 'card_brand', 'card_type', 'card_number', 'cvv', 'card_issue_date', 'card_expiration_date']

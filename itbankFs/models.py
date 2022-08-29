from django.db import models

# Create your models here.

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    direccion = models.TextField()

# Clientes
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Sucursal, models.DO_NOTHING)
    directions = models.TextField()


# Cuenta
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()


# Prestamos


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

# Tarjetas
class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField(unique=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    cvv = models.IntegerField()
    creation_date = models.TextField()
    expire_date = models.TextField()
    card_type = models.TextField()
    brand = models.TextField()
    client_type = models.TextField()

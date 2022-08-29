from django.db import models

# Create your models here.
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


# class Sucursal(models.Model):
#     branch_id = models.AutoField(primary_key=True)
#     branch_number = models.BinaryField()
#     branch_name = models.TextField()
#     branch_address_id = models.IntegerField()
#     direccion = models.TextField()

#     class Meta:

#         verbose_name = "Sucursal"
#         verbose_name_plural = "Sucursales"
        
#     def __str__(self):
#         return self.branch_id

# # Clientes
# class Cliente(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     customer_name = models.TextField()
#     customer_surname = models.TextField()
#     customer_dni = models.TextField(db_column='customer_DNI')
#     dob = models.TextField(blank=True, null=True)
#     branch = models.ForeignKey(Sucursal, models.DO_NOTHING)
#     directions = models.TextField()

#     class Meta:
#         verbose_name = "Cliente"
#         verbose_name_plural = "Clientes"
        
#     def __str__(self):
#         return self.customer_id


# # Cuenta
# class Cuenta(models.Model):
#     account_id = models.AutoField(primary_key=True)
#     customer_id = models.IntegerField()
#     balance = models.IntegerField()
#     iban = models.TextField()

#     class Meta:
#         verbose_name = "Cuenta"
#         verbose_name_plural = "Cuentas"
        
#     def __str__(self):
#         return self.account_id


# # Prestamos
# class Prestamo(models.Model):
#     loan_id = models.AutoField(primary_key=True)
#     loan_type = models.TextField()
#     loan_date = models.TextField()
#     loan_total = models.IntegerField()
#     customer_id = models.IntegerField()

#     class Meta:
#         verbose_name = "Prestamo"
#         verbose_name_plural = "Prestamos"
        
#     def __str__(self):
#         return self.loan_id

# # Tarjetas
# class Tarjeta(models.Model):
#     card_id = models.AutoField(primary_key=True)
#     card_number = models.IntegerField(unique=True)
#     customer = models.ForeignKey(Cliente, models.DO_NOTHING)
#     cvv = models.IntegerField()
#     creation_date = models.TextField()
#     expire_date = models.TextField()
#     card_type = models.TextField()
#     brand = models.TextField()
#     client_type = models.TextField()

#     class Meta:
#         verbose_name = "Tarjeta"
#         verbose_name_plural = "Tarjetas"
        
#     def __str__(self):
#         return self.card_id

from django.contrib import admin
from .models import Sucursal, Cliente, Cuenta, Tarjeta,Prestamo, TipoCliente
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Prestamo)
admin.site.register(Tarjeta)
admin.site.register(Sucursal)
admin.site.register(TipoCliente)
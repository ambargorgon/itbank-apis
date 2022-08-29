from django.shortcuts import render

from django.contrib.auth.models import User


from .forms import loginForm, RegisterForm, Prestamos
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from .models import Cuenta, Cliente, Tarjeta


# Create your views here.
formLogin = loginForm()
formRegister = RegisterForm()


def userLogin(request):
    if request.method == 'POST':

        # dentro del template del form, está el nombre "register" dentro del submit del form
        # de esta manera podemos diferenciar cuál es el formulario que se está enviando
        if 'register' in request.POST:

            dni = request.POST['dni']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            # se chequea que las contraseñas coincidan
            if password == password2:

                # se crea el usuario con los datos ingresados
                # user = User.objects.create_user()
                user = User.objects.create_user(
                    username=dni, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()

                messages.success(request, 'Usuario creado correctamente')

                return HttpResponseRedirect('/')

            else:

                messages.error(request, 'Pin incorrecto')

                return HttpResponseRedirect('/')

        # si se completó el formulario de login
        if 'login' in request.POST:

            dni = request.POST['dni']
            password = request.POST['password']
            user = authenticate(username=dni, password=password)

            if user is not None and password is not None:

                login(request, user)

                return HttpResponseRedirect('/')

            else:

                messages.error(request, 'Usuario o contraseña incorrectos')
                return HttpResponseRedirect('/')

        if 'logaut' in request.POST:
            logout(request)
            return HttpResponseRedirect('/')


def home(request):
    userLogin(request)
    return render(request, 'index.html', {'form': formLogin, 'formRegister': formRegister})


def prestamos(request):
    prestamos = Prestamos()
    userLogin(request)
    if request.user.is_authenticated:
        user = Cliente.objects.get(
            customer_dni=User.get_username(request.user))
        tarjeta = Tarjeta.objects.get(customer_id=user.customer_id)
        if tarjeta.client_type == 'CLASSIC':
                limit = '100000'
        elif  tarjeta.client_type == 'GOLD':
                limit = '300000'
        elif  tarjeta.client_type == 'BLACK':
                limit = '500000'
        if request.method == 'POST':
            cantidad = request.POST['cantidad']
            motivo = request.POST['motivo']
            if cantidad >= limit:
                print('La cantidad supera el limite')
                return HttpResponseRedirect('/prestamos')
            else:
                print('PASA')
                return HttpResponseRedirect('/prestamos')

    return render(request, 'prestamos.html', {'form': formLogin, 'formRegister': formRegister, 'prestamos': prestamos})


def atCliente(request):
    userLogin(request)
    return render(request, 'atCliente.html', {'form': formLogin, 'formRegister': formRegister})


def seguros(request):
    userLogin(request)
    return render(request, 'seguros.html', {'form': formLogin, 'formRegister': formRegister})


def tarjetas(request):
    userLogin(request)
    return render(request, 'tarjetas.html', {'form': formLogin, 'formRegister': formRegister})


def dolarHoy(request):
    userLogin(request)
    return render(request, 'dolarHoy.html', {'form': formLogin, 'formRegister': formRegister})


def calculadora(request):
    userLogin(request)
    return render(request, 'calculadora.html', {'form': formLogin, 'formRegister': formRegister})


def cuentas(request):
    userLogin(request)
    return render(request, 'cuentas.html', {'form': formLogin, 'formRegister': formRegister})


def clientes(request):
    print(Cliente.objects.all())
    userLogin(request)
    if request.user.is_authenticated:
        user = Cliente.objects.get(customer_dni=User.get_username(request.user))
        cuenta = Cuenta.objects.get(account_id=user.customer_id)
        tarjeta = Tarjeta.objects.get(customer_id=user.customer_id)
        # print(tarjeta)
        context = {
            "user": user,
            "cuenta": cuenta,
            'tarjeta': tarjeta
        }
    else:
        context = {}
    return render(request, 'clientes.html', {'form': formLogin, 'formRegister': formRegister, 'context': context})

@login_required
def homebanking(request):
    
    prestamos = Prestamos()
    userLogin(request)
    if request.user.is_authenticated:

        user = Cliente.objects.get(customer_dni=User.get_username(request.user))
        tarjeta = Tarjeta.objects.get(customer_id=user.customer_id)

        if tarjeta.client_type == 'CLASSIC':
                limit = '100000'

        elif tarjeta.client_type == 'GOLD':
                limit = '300000'

        elif tarjeta.client_type == 'GOLD':
                limit = '500000'

        if request.method == 'POST':
            cantidad = request.POST['cantidad']
            motivo = request.POST['motivo']

            if cantidad >= limit:
                    print('La cantidad supera el limite')
                    messages.error(request, 'La cantidad solicitada supera el limite. Por favor intente con una cantidad menor, o suba su plan')
                    return HttpResponseRedirect('/homebanking')
            else:
                messages.success(request, '¡Prestamo aprobado!')
                return HttpResponseRedirect('/homebanking')

        user = Cliente.objects.get(customer_dni=User.get_username(request.user))
        cuenta = Cuenta.objects.get(account_id=user.customer_id)
        tarjeta = Tarjeta.objects.get(customer_id=user.customer_id)
        # print(tarjeta)
        context = {
            "user": user,
            "cuenta": cuenta,
            'tarjeta': tarjeta,
        }

    else:
        context = {}

    return render(request, 'homebanking.html', {'context': context, 'prestamos': prestamos})

from django import forms


class loginForm(forms.Form):
    dni = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'DNI'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password', 'type': 'password'}))


class RegisterForm(forms.Form):
    dni = forms.CharField(required=True,
                          widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'DNI'}))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'Apellido'}))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'email'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Password', 'type': 'password'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Repeat Password', 'type': 'password'}))


class Prestamos(forms.Form):
    cantidad = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'imput-text', 'placeholder': 'Cantidad'}))
    motivo = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'imput-text', 'placeholder': 'Motivo'}))
    # dni = forms.CharField(required=True, widget=forms.TextInput(
    #     attrs={'class': 'imput-text', 'placeholder': 'Dni'}))
    # pin = forms.CharField(required=True, widget=forms.TextInput(
    #     attrs={'class': 'imput-text', 'placeholder': 'Pin'}))

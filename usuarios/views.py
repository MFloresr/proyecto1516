# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib import messages

from .forms import Login_Form, RegistForm
from django.contrib.auth.models import User

def registrar(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')
            usuario = User()
            usuario.username = username
            usuario.set_password(password)
            usuario.email = email
            usuario.save()
            messages.success(request, 'Usuario Registrado')
            return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Usuario no existe')
    else:
        
        form = RegistForm()
        
    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-6 col-md-offset-3'
    form.helper.label_class = 'col-lg-2'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', { 'form': form })
    
def vista_login(request):
    if request.method=='POST': #SI LO ENVIADO ES UN POST...
        form = Login_Form(request.POST) #Captura del formulari
        if form.is_valid(): #METODO QUE DICE QUE EL FORMULARIO ES VALIDO (POR NO ENTRADO, SIMBOLOS, LETRAS EN LUGAR DE NUMEROS...)
            username = form.cleaned_data['username'] #Captura el nombre de usuario del formulario
            password = form.cleaned_data['password'] #Captura el padsword del formulario
            seguent = request.GET.get('next', default=None)  #Captura una posible continuación del usuario (donde queria ir)
            user = authenticate(username=username, password=password)  #Si NO es nada...
            if user is not None: #Si existe el usuario...
                if user.is_active: #Si esta activo ...
                    login(request, user) #Autentifica el usuario
                    if bool( seguent ): #Si estava en una url y le ha pedido autentificació
                        messages.success(request, 'Bienvenido ' + username + '!')
                        return HttpResponseRedirect( seguent ) #Rediridige al usuario donde queria ir
                    else:
                        messages.success(request, 'Bienvenido ' + username + '!')
                        return HttpResponseRedirect( reverse( 'noticias:ver_noticias' )  )  #Lo envias a la pagina que tu quieras
                else: #Error en el usuario, no esta activo
                    return HttpResponse("Usuario no activo")
            else: #El usuario no es correcto
                messages.error(request, "Usuario o contraseña incorrecto") #Redireccionas de nuevo al login y muestras un mensaje de error
                return HttpResponseRedirect(vista_login)
                
    else: #No es un post, genera el formulario
        form = Login_Form()
    
    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-6 col-md-offset-3'
    form.helper.label_class = 'col-lg-2'
    
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form':form, 'titol':"Login",'h1':"Login"}) #Renderiza el formulario en el login.html
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Ja has sortit del teu compte')
    return HttpResponseRedirect(reverse('login'))
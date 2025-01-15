import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

# Create your views here.
def validar_email(email):
    try:
        
        User.objects.get(email=email)
        
        raise ValidationError('Este correo electrónico ya está en uso.')
    except User.DoesNotExist:
        
        pass



def register(request ):
  if request.method =='POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username= request.POST['username']
    email= request.POST['email']
    password= request.POST['password']
    password2= request.POST['password2']
    
    if not re.match(r'^[A-Z][a-z]*$', first_name):
            messages.info(request, 'El campo solo permite una palabra, no permite ni caracteres especiales ni numeros, debe iniciar con una letra mayuscula y la siguientes minusculas.', extra_tags='first_name_error')
            return HttpResponseRedirect('/register/')
          
    if not re.match(r'^[A-Z][a-z]*$', last_name):
            messages.info(request, 'El campo solo permite una palabra, no permite ni caracteres especiales ni numeros, debe iniciar con una letra mayuscula y la siguientes minusculas.', extra_tags='last_name_error')
            return HttpResponseRedirect('/register/')
    
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request,'Usuario ya Existe', extra_tags='username_exists')
        return HttpResponseRedirect('/register/')
      else:
        try:
          validar_email(email)  
        except ValidationError as e:
          messages.info(request, e.message, extra_tags='email_error')  
          return HttpResponseRedirect('/register/')
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name, email=email, password=password)
        user.save()
        messages.info(request,'Usuario Creado Exitosamente')
        return HttpResponseRedirect('/login/')
        
    else:
      messages.info(request,'Contraseña No Coinciden', extra_tags='password_error')
      return HttpResponseRedirect('/register/')
    
  
  return render(request, 'base/register.html')

def login(request):
  
  if request.method == 'POST':
    email= request.POST['email']
    password= request.POST['password']
    username = User.objects.get(email=email).username
    user= auth.authenticate(username=username,password=password)
    
    if user is not None:
      auth.login(request,user)
      return HttpResponseRedirect('http://127.0.0.1:8000/home/')
    else:
      messages.info(request,'Error al Ingresar Informacion Incorrecta')
      return HttpResponseRedirect('http://127.0.0.1:8000/login/')
  
  return render(request,'base/login2.html')

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('http://127.0.0.1:8000/login/')

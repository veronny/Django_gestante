from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

# Create your views here.
from .forms import FiliacionForm, DirectorioForm
from .models import Filiacion, Directorio,Provincia, Distrito, Red, Microred, Establecimiento

def home(request):
    return render(request, 'home.html')

# ----- DIRECTORIO MUNICIPIO --------------------
@login_required
def filiacion(request):
    filiaciones = Filiacion.objects.all()
    context = {
                'filiaciones': filiaciones,
                }
    return render(request, 'filiacion.html', context)

@login_required
def create_filiacion(request):
    if request.method == "GET":
        return render(request, 'create_filiacion.html', {
            "form": FiliacionForm
        })
    else:
        try:
            form = FiliacionForm(request.POST, request.FILES)
            new_filiacion = form.save(commit=False)
            new_filiacion.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'create_filiacion.html', {
                "form": FiliacionForm,
                "error": "Error creating task."
            })

@login_required
def filiacion_detail(request, filiacion_id):
    if request.method == 'GET':
        filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
        form = FiliacionForm(instance=filiacion)
        context = {
            'filiacion': filiacion,
            'form': form
        }
        return render(request, 'filiacion_detail.html', context)
    else:
        try:
            filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
            form = FiliacionForm(request.POST,request.FILES, instance=filiacion)
            form.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'filiacion_detail.html', {'filiacion': filiacion, 'form': form, 'error': 'Error actualizar'})

@login_required
def delete_filiacion(request, filiacion_id):
    filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
    if request.method == 'POST':
        filiacion.delete()
        return redirect('filiacion')

# ----- DIRECTORIO SALUD DIRESA --------------------
@login_required
def directorio_diresa(request):
    directorio_diresas = Directorio.objects.all()
    context = {
                'directorio_diresas': directorio_diresas,
                }
    return render(request, 'directorio_diresa.html', context)

@login_required
def create_directorio_diresa(request):
    if request.method == "GET":
        return render(request, 'create_directorio_diresa.html', {
            "form": DirectorioForm
        })
    else:
        try:
            form = DirectorioForm(request.POST, request.FILES)
            new_directorio = form.save(commit=False)
            new_directorio.save()
            return redirect('create_directorio_diresa')
        except ValueError:
            return render(request, 'create_directorio_diresa.html', {
                "form": DirectorioForm,
                "error": "Error creating task."
            })

@login_required
def directorio_diresa_detail(request, directorio_diresa_id):
    if request.method == 'GET':
        directorio_diresa = get_object_or_404(Directorio, pk=directorio_diresa_id)
        form = DirectorioForm(instance=directorio_diresa)
        context = {
            'directorio_diresa': directorio_diresa,
            'form': form
        }
        return render(request, 'directorio_diresa_detail.html', context)
    else:
        try:
            directorio_diresa = get_object_or_404(Directorio, pk=directorio_diresa_id)
            form = DirectorioForm(request.POST,request.FILES, instance=directorio_diresa)
            form.save()
            return redirect('directorio_salud')
        except ValueError:
            return render(request, 'directorio_diresa_detail.html', {'directorio_diresa': directorio_diresa, 'form': form, 'error': 'Error actualizar'})

# ----- DIRECTORIO SALUD RED --------------------
@login_required
def directorio_red(request):
    directorio_red = Directorio.objects.all()
    context = {
                'directorio_red': directorio_red,
                }
    return render(request, 'directorio_red.html', context)

# ----- DIRECTORIO SALUD ESTABLECIMIENTO --------------------
def directorio_establecimiento(request):
    directorio_establecimiento = Directorio.objects.all()
    context = {
                'directorio_establecimiento': directorio_establecimiento,
                }
    return render(request, 'directorio_establecimiento.html', context)


# ----- INICIO DE SESION --------------------------------
@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('filiacion')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('filiacion')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password fo not match'
        })

# ----- SELECT DEPENDIENTES FILIACION --------------------
def distrito(request):
    provincias = request.GET.get('provincia_selected')
    distritos = Distrito.objects.filter(provincia_id=provincias)
    context = {
                'distritos': distritos, 
                'is_htmx': True 
                }
    return render(request, 'partials/distritos.html', context)

# ----- FRONTEND FILIACION --------------------
def frontend_filiacion(request):
    filiaciones = Filiacion.objects.all()
    context = {
            'filiaciones': filiaciones,
            }
    return render(request, 'frontend/filiacion.html', context)

def frontend_directorio_diresa(request):
    directorio_diresas= Directorio.objects.all()
    context = {
            'directorio_diresas': directorio_diresas,
            }
    return render(request, 'frontend/directorio_diresa.html', context)
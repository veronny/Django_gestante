from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import FiliacionForm
from .models import Filiacion


def home(request):
    return render(request, 'home.html')


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

@login_required
def filiacion(request):
    filiaciones = Filiacion.objects.all()
    return render(request, 'filiacion.html', {'filiaciones': filiaciones})

@login_required
def create_filiacion(request):
    if request.method == "GET":
        return render(request, 'create_filiacion.html', {
            "form": FiliacionForm
        })
    else:
        try:
            form = FiliacionForm(request.POST)
            new_filiacion = form.save(commit=False)
        #    new_filiacion.user = request.user
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
        return render(request, 'filiacion_detail.html', {'filiacion': filiacion, 'form': form})
    else:
        try:
            filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
            form = FiliacionForm(request.POST, instance=filiacion)
            form.save()
            return redirect('filiacion')
        except ValueError:
            return render(request, 'filiacion_detail.html', {'filiacion': filiacion, 'form': form, 'error': 'Error updating task.'})

@login_required
def delete_filiacion(request, filiacion_id):
    filiacion = get_object_or_404(Filiacion, pk=filiacion_id)
    if request.method == 'POST':
        filiacion.delete()
        return redirect('filiacion')

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

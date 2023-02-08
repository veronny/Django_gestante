from django.forms import ModelForm
from .models import Filiacion, Directorio, DirectorioRed, DirectorioEstablecimiento
from django import forms

class FiliacionForm(forms.ModelForm):
    class Meta:
       model =  Filiacion       
       fields = [
                 'provincia',
                 'distrito',
                 'tipo_municipalidad',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'provincia' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'distrito' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'tipo_municipalidad' : forms.Select(attrs={'class': 'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }

class DirectorioForm(forms.ModelForm):
    class Meta:
       model =  Directorio       
       fields = [
                 'diresa',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'diresa' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }
       
class DirectorioRedForm(forms.ModelForm):
    class Meta:
       model =  DirectorioRed    
       fields = [
                 'red',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'red' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }

class DirectorioEstablecimientoForm(forms.ModelForm):
    class Meta:
       model =  DirectorioEstablecimiento   
       fields = [
                 'red',
                 'microred',
                 'establecimiento',
                 'documento_identidad',
                 'apellido_paterno',
                 'apellido_materno',
                 'nombres',
                 'telefono',
                 'correo_electronico',
                 'perfil', 
                 'condicion',
                 'cuenta_usuario',
                 'req_formato',
                 'req_generales_excel'
                ]
             
       widgets = {
                'red' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'microred' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'establecimiento' : forms.TextInput(attrs={'class':'form-control','style': 'border-color: silver; color: silver;','readonly':'readonly'}),
                'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
                'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
                'nombres' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control'}),
                'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
                'perfil' : forms.Select(attrs={'class':'form-control'}),
                'condicion' : forms.Select(attrs={'class':'form-control'}),
                'cuenta_usuario' : forms.Select(attrs={'class':'form-control'}),
                'req_formato' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'req_generales_excel' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
       }
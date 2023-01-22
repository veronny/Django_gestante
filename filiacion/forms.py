from django.forms import ModelForm
from .models import Filiacion
from django import forms

class FiliacionForm(forms.ModelForm):
    class Meta:
       model =  Filiacion
       fields = ['numero_documento','historia_clinica','apellido_paterno','apellido_materno','nombres','direccion_reniec','direccion_declarado','ubigeo_reniec','ubigeo_declarado','fecha_nacimiento','edad','fecha_ultima_regla','fecha_probable_parto','numero_telefono']
       widgets = {
           'numero_documento' : forms.TextInput(attrs={'class':'form-control'}),
           'historia_clinica' : forms.TextInput(attrs={'class':'form-control'}),
           'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
           'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
           'nombres' : forms.TextInput(attrs={'class':'form-control'}),
           'direccion_reniec' : forms.TextInput(attrs={'class':'form-control'}),
       }
    
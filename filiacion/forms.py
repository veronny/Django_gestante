from django.forms import ModelForm
from .models import Filiacion
from django import forms

class FiliacionForm(forms.ModelForm):
    class Meta:
       model =  Filiacion
       fields = ['provincia','distrito','tipo_municipalidad','documento_identidad','apellido_paterno','apellido_materno','nombres','telefono','correo_electronico','perfil','condicion','cuenta_usuario','contraseña_usuario','req_oficio', 'req_resolucion','req_formato','req_generales_excel']
       widgets = {
           'provincia' : forms.TextInput(attrs={'class':'form-control'}),
           'distrito' : forms.TextInput(attrs={'class':'form-control'}),
           'tipo_municipalidad' : forms.TextInput(attrs={'class':'form-control'}),
           'documento_identidad' : forms.TextInput(attrs={'class':'form-control'}),
           'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
           'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
           'nombres' : forms.TextInput(attrs={'class':'form-control'}),
           'telefono' : forms.TextInput(attrs={'class':'form-control'}),
           'correo_electronico' : forms.TextInput(attrs={'class':'form-control'}),
           'perfil' : forms.TextInput(attrs={'class':'form-control'}),
           'condicion' : forms.TextInput(attrs={'class':'form-control'}),
           'cuenta_usuario' : forms.TextInput(attrs={'class':'form-control'}),
           'contraseña_usuario' : forms.TextInput(attrs={'class':'form-control'}),
           'req_oficio' : forms.TextInput(attrs={'class':'form-control'}),
           'req_resolucion' : forms.TextInput(attrs={'class':'form-control'}),
           'req_formato' : forms.TextInput(attrs={'class':'form-control'}),
           'req_generales_excel' : forms.TextInput(attrs={'class':'form-control'}),
       }
    
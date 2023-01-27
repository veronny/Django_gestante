from django.db import models

# Create your models here.
class Filiacion(models.Model):
    provincia = models.CharField(max_length=20,null=True, blank=True)
    distrito = models.CharField(max_length=20,null=True, blank=True)
    tipo_municipalidad = models.CharField(max_length=100,null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(max_length=100,null=True, blank=True)
    condicion = models.CharField(max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_oficio = models.CharField(max_length=100,null=True, blank=True)
    req_resolucion = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.CharField(max_length=100,null=True, blank=True)
    req_generales_excel = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
from django.db import models

# Create your models here.
class Filiacion(models.Model):
    numero_documento = models.CharField(max_length=20,null=True, blank=True)
    historia_clinica = models.CharField(max_length=20,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=100,null=True, blank=True)
    nombres = models.CharField(max_length=100,null=True, blank=True)
    direccion_reniec = models.CharField(max_length=200,null=True, blank=True)
    direccion_declarado = models.CharField(max_length=200,null=True, blank=True)
    ubigeo_reniec = models.CharField(max_length=200,null=True, blank=True)
    ubigeo_declarado = models.CharField(max_length=200,null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=100,null=True, blank=True)
    edad = models.CharField(max_length=100,null=True, blank=True)
    fecha_ultima_regla = models.CharField(max_length=100,null=True, blank=True)
    fecha_probable_parto = models.CharField(max_length=100,null=True, blank=True)
    numero_telefono = models.CharField(max_length=100,null=True, blank=True)
    id_establecimiento = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
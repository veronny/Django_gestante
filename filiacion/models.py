from django.db import models

class Red(models.Model):
    nombre_red = models.CharField(max_length=100, default="", null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="", null=True, blank=True)
    def __str__(self):
        return self.nombre_red   
class Microred(models.Model):
    nombre_microred = models.CharField(max_length=100,null=True, blank=True)
    cod_mic = models.CharField(max_length=10, default="",null=True, blank=True)
    cod_red = models.CharField(max_length=10, default="",null=True, blank=True)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, related_name='redes',null=True, blank=True)  
    def __str__(self):
        return self.nombre_microred   
class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=100, null=True, blank=True)
    codigo_unico = models.CharField(max_length=100, default="", null=True, blank=True)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, null=True, blank=True)
    microred = models.ForeignKey(Microred, on_delete=models.CASCADE, related_name='microredes', null=True, blank=True)  
    def __str__(self):
        return self.nombre_establecimiento     
class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=100,null=True, blank=True)
    ubigeo = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nombre_provincia        
class Distrito(models.Model):
    nombre_distrito = models.CharField(max_length=100, null=True, blank=True)
    ubigeo = models.CharField(max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='provincias', null=True, blank=True)  
    def __str__(self):
        return self.nombre_distrito
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
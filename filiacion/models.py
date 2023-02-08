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
    TIPO_MUNICIPALIDAD = [
                ('Provincial', 'Provincial'),
                ('Distrital', 'Distrital'),
            ]
    
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    provincia = models.CharField(max_length=100,null=True, blank=True)
    distrito = models.CharField(max_length=100,null=True, blank=True)
    tipo_municipalidad = models.CharField(choices=TIPO_MUNICIPALIDAD, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class Directorio(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    

class DirectorioRed(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
class DirectorioEstablecimiento(models.Model):
    TIPO_USUARIO = [
                    ('diresa', 'diresa'),
                    ('red', 'red'),
                    ('microred', 'microred'),
                    ('establecimiento', 'establecimiento'),
                ]
         
    PERFIL = [
                ('Consultor', 'Consultor'),
                ('Registrador', 'Registrador'),
            ]
  
    CONDICION = [
                    ('Alta', 'Alta'),
                    ('Baja', 'Baja'),
                ]

    CUENTA_USUARIO = [
                    ('Si', 'Si'),
                    ('No', 'No'),
                    ('Espera respuesta MINSA', 'Espera respuesta MINSA'),
                ]
    
    diresa = models.CharField(max_length=100,null=True, blank=True)
    red = models.CharField(max_length=100,null=True, blank=True)
    microred = models.CharField(max_length=100,null=True, blank=True)
    establecimiento = models.CharField(max_length=100,null=True, blank=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100, null=True, blank=True)
    documento_identidad = models.CharField(max_length=100,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100,null=True, blank=True)
    apellido_materno = models.CharField(max_length=200,null=True, blank=True)
    nombres = models.CharField(max_length=200,null=True, blank=True)
    telefono = models.CharField(max_length=200,null=True, blank=True)
    correo_electronico = models.CharField(max_length=200,null=True, blank=True)
    perfil = models.CharField(choices=PERFIL,max_length=100,null=True, blank=True)
    condicion = models.CharField(choices=CONDICION,max_length=100,null=True, blank=True)
    cuenta_usuario = models.CharField(choices=CUENTA_USUARIO,max_length=100,null=True, blank=True)
    contraseña_usuario = models.CharField(max_length=100,null=True, blank=True)
    req_formato = models.FileField(upload_to="filiacion/formato/",null=True, blank=True)
    dateTimeOfUpload_req_formato = models.DateTimeField(auto_now = True,null=True, blank=True)
    req_generales_excel = models.FileField(upload_to="filiacion/excel/",null=True, blank=True)
    dateTimeOfUpload_generales_excel = models.DateTimeField(auto_now = True,null=True, blank=True)
    
    def __str__(self):
        return self.nombres
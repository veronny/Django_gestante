from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Filiacion, Red, Microred, Establecimiento, Provincia, Distrito

# Register your models here.

@admin.register(Filiacion)
class FiliacionAdmin(admin.ModelAdmin):
    list_display = (
        'documento_identidad',
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'telefono',
        'correo_electronico',
    )
    search_fields = ('nombres',)

# Red
class RedResources(resources.ModelResource):
    class Meta:
        model = Red

@admin.register(Red)
class RedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RedResources
    list_display = (
        'id',
        'nombre_red',
        'cod_red',
    )
    search_fields = ('nombre_red',)

# Red
admin.site.register(Microred)

# Establecimiento
class EstablecimientoResources(resources.ModelResource):
    class Meta:
        model = Establecimiento

@admin.register(Establecimiento)
class EstablecimientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = EstablecimientoResources
    list_display = (
        'id',
        'nombre_establecimiento',
        'codigo_unico',
        'red',
        'microred',
    )
    search_fields = ('nombre_establecimiento',)
    
# Provincia  
class ProvinciaResources(resources.ModelResource):
    class Meta:
        model = Provincia
@admin.register(Provincia)
class ProvinciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ProvinciaResources
    list_display = (
        'id',
        'nombre_provincia',
        'ubigeo',
    )
    search_fields = ('nombre_provincia',)

# Distrito
class DistritoResources(resources.ModelResource):
    class Meta:
        model = Distrito

@admin.register(Distrito)
class DistritoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = DistritoResources
    list_display = (
        'id',
        'nombre_distrito',
        'ubigeo',
        'provincia',
    )
    search_fields = ('nombre_distrito',)
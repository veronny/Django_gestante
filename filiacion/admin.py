from django.contrib import admin
from .models import Filiacion, Red, Microred, Establecimiento, Provincia, Distrito

# Register your models here.

admin.site.register(Filiacion)
admin.site.register(Red)
admin.site.register(Microred)
admin.site.register(Establecimiento)
admin.site.register(Provincia)
admin.site.register(Distrito)

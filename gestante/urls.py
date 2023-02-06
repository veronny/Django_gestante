from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from filiacion import views 
# Subir archivos estaticos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    # directorio gobierno local
    path('filiacion/', views.filiacion, name='filiacion'),
    path('filiacion/create/', views.create_filiacion, name='create_filiacion'),
    path('filiacion/<int:filiacion_id>/', views.filiacion_detail, name='filiacion_detail'),
    path('filiacion/<int:filiacion_id>/delete', views.delete_filiacion, name='delete_filiacion'),
    # directorio salud DIRESA
    path('directorio_salud/', views.directorio_diresa, name='directorio_salud'),
    path('directorio/create/', views.create_directorio_diresa, name='create_directorio_diresa'),
    path('directorio/<int:directorio_diresa_id>/', views.directorio_diresa_detail, name='directorio_diresa_detail'),
   # path('create_directorio/<int:directorio_salud_id>/delete', views.delete_directorio_salud, name='delete_directorio_salud'),
    # directorio salud RED
    
    # directorio salud ESTABLECIMIENTOS
    
    #frontend routes
    path('frontend_filiacion/', views.frontend_filiacion, name='frontend_filiacion'),
    path('frontend_directorio_diresa/', views.frontend_directorio_diresa, name='frontend_directorio_diresa'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
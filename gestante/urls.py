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
    path('filiacion/', views.filiacion, name='filiacion'),
    path('filiacion/create/', views.create_filiacion, name='create_filiacion'),
    path('filiacion/<int:filiacion_id>/', views.filiacion_detail, name='filiacion_detail'),
    path('filiacion/<int:filiacion_id>/delete', views.delete_filiacion, name='delete_filiacion'),
    
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    
    #frontend routes
    path('frontend_filiacion/', views.frontend_filiacion, name='frontend_filiacion'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
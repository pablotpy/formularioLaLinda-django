from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
     path('',views.formulario,name="formulario"),
     path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
     
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
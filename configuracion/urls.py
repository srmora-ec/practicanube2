from django.contrib import admin
from django.urls import path
from inicio.views import hola_mundo  # Importamos tu función

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', hola_mundo),             
]
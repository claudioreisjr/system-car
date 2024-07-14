#criar urls que estao dentro de usuarios
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
  
]
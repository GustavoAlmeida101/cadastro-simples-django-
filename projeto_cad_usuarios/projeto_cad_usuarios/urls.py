
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    
    # rota,view responsavél,nome de refênrecia
    # usuario.com
    path('', views.home, name='home'),
    # usuario.com
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]

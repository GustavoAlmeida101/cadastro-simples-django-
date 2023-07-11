from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # salvar os dados na tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # exibir todos os usuarios cadastrado em uma pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retornar os dados para a pagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)

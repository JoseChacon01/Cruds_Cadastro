from django.shortcuts import render
from .models import Produto #".models" pois é um arquivo do mesmo diretorio

def listar_produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render (request, 'produtos.html', contexto)


def cadastrar_produto(request):
    return render (request, 'produto_cadastrar.html')
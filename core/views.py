
from multiprocessing import contexto
from django.shortcuts import render, redirect
from .models import Produto #".models" pois é um arquivo do mesmo diretorio
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render (request, 'produtos.html', contexto)


def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)
    contexto = {
        'form_produto': form
    }
    return render (request, 'produto_cadastrar.html', contexto)
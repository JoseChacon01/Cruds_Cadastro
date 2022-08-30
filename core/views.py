
from django.shortcuts import render, redirect
from .models import Produto #".models" pois é um arquivo do mesmo diretorio
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render (request, 'produtos.html', contexto)

def opcao_produto(request):
    return render   (request, 'opcao.html')      

def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():#Se o formulario for preenchido e todos os dados forem validos, SALVE.
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produto': form
    }
    return render (request, 'produto_cadastrar.html', contexto)

 
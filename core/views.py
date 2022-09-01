
from django.shortcuts import render, redirect
from .models import Fornecedor, Produto, Cliente, Fornecedor #".models" pois é um arquivo do mesmo diretorio, esta importando para views as classes criadas em models.py
from .forms import ProdutoForm, ClienteForm, FornecedorForm

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

def editar_produto(request, id):
    produto = Produto.objects.get(pk=id)

    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produto': form
    }

    return render(request, 'produto_cadastrar.html', contexto)

def remover_produto(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('listar_produtos')

# def index(request):
#     return render(request, 'index.html', contexto)

#Clientes
def listar_clientes(request):       
    clientes = Cliente.objects.all()
    contexto = {
        'todos_clientes': clientes
    }
    return render (request, 'clientes.html', contexto)


def cadastrar_cliente(request):     
    form = ClienteForm(request.POST or None)

    if form.is_valid(): #Se os dados forem validos, salve o formulario
        form.save()
        return redirect('listar_clientes') # e redirecione o usuario para pagina de listagem

    contexto = {
        'form_cliente': form
    }
    return render(request, 'cliente_cadastrar.html', contexto)

def editar_cliente(request, id): #EDITAR dados do Cliente
    cliente = Cliente.objects.get(pk=id)

    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')

    contexto = {
        'form_cliente': form
    }    

    return render (request, 'cliente_cadastrar.html', contexto)


def remover_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect('listar_clientes')


#Fornecedores
def listar_fornecedores(request):       
    fornecedores = Fornecedor.objects.all()
    contexto = {
        'todos_fornecedores': fornecedores
    }
    return render (request, 'fornecedores.html', contexto)


def cadastrar_fornecedor(request):     
    form = FornecedorForm(request.POST or None)

    if form.is_valid(): #Se os dados forem validos, salve o formulario
        form.save()
        return redirect('listar_fornecedores') # e redirecione o usuario para pagina de listagem

    contexto = {
        'form_fornecedor': form
    }
    return render(request, 'fornecedor_cadastrar.html', contexto)

def editar_fornecedor(request, id): #EDITAR dados do fornecedor
    fornecedor = Fornecedor.objects.get(pk=id)

    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')

    contexto = {
        'form_fornecedor': form
    }    

    return render (request, 'fornecedor_cadastrar.html', contexto)


def remover_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    fornecedor.delete()
    return redirect('listar_fornecedores')
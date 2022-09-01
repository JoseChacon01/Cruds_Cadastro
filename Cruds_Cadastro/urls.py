"""Cruds_Cadastro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_clientes, listar_produtos, cadastrar_produto, opcao_produto, editar_produto, remover_produto
from core.views import listar_clientes, cadastrar_cliente, editar_cliente, remover_cliente
from core.views import listar_fornecedores, cadastrar_fornecedor, editar_fornecedor, remover_fornecedor

urlpatterns = [
    path('opcao_cadastro/', opcao_produto, name= 'opcao_produto'),
    path('produtos/', listar_produtos, name= 'listar_produtos'),
    path('produto_cadastrar/', cadastrar_produto, name= 'cadastrar_produto'),
    path('produto_editar/<int:id>/', editar_produto, name='editar_produto'),
    path('produto_remover/<int:id>/', remover_produto, name='remover_produto'),
    path('admin/', admin.site.urls),
    path('clientes/', listar_clientes, name='listar_clientes'),#Clientes
    path('clinte_cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente_editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('cliente_remover/<int:id>/', remover_cliente, name='remover_cliente'),
    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'), #Fornecedores
    path('fornecedor_cadastrar/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedor_editar/<int:id>/', editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor_remover/<int:id>/', remover_fornecedor, name='remover_fornecedor'),
    ]

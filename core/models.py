from distutils.command.upload import upload
from django.db import models


class Produto(models.Model): #Tabela Produtos
    produto = models.CharField('Produto', max_length=100) #Colunas
    estilo = models.CharField('Estilo', max_length=100)
    marca = models.CharField('Marca', max_length=50)
    quantidade = models.IntegerField('Quantidade')
    imagem = models.ImageField(upload_to='produto/')


#Tabela Cliente
class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    endereco = models.CharField('endereco', max_length=200)
   # nascimento = models.CharField('nascimento', max_length=10)
    email = models.EmailField('email')

#Tabela Fornecedor
class Fornecedor(models.Model):
    nome = models.CharField('nome', max_length=100)   
    endereco = models.CharField('endereco', max_length=200)
    email = models.EmailField('email')
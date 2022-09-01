from dataclasses import fields
from django.forms import ModelForm
from .models import Produto, Cliente, Fornecedor

# Criando os campos altomaticamente com o "modelsForm"
class ProdutoForm(ModelForm): #Criando o formulario da tabela "Produto"
    class Meta:
        model = Produto
        fields = ['produto', 'estilo', 'marca', 'quantidade']

#Cliente
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'email']

#Fornecedor
class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'endereco', 'email']

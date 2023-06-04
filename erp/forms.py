from django import forms

from erp.models import Funcionario, Produto


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email_funcional',
            'remuneracao'
        ]
    
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'descricao': 'Descrição',
            'preco': 'Preço'
        }
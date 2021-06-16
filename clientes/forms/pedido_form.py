from ..models import Pedido, Cliente, Produto
from django import forms


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all()) #faz um campo de escolha com as instancias do objeto
    observacoes = forms.CharField(widget=forms.Textarea)  #cria um widget para editar o input do formulario
    produto = forms.ModelMultipleChoiceField(queryset=Produto.objects.all()) #seleciona mais de uma instancia do objeto

    class Meta:
        model = Pedido
        fields = ['cliente', 'data_pedido', 'valor', 'status', 'observacoes', 'produto']
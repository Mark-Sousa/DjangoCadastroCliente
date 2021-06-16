from clientes.models import Cliente
from django.forms import ModelForm


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'data_nascimento', 'email', 'profissao', 'sexo', 'rua', 'numero', 'complemento', 'bairro',
            'cidade', 'pais'
        ]
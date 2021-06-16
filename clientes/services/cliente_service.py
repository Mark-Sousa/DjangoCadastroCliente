from clientes.models import Cliente


def listar_todos_clientes():
    return Cliente.objects.all()


def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, data_nascimento=cliente.data_nascimento, email=cliente.email,
                           profissao=cliente.profissao, sexo=cliente.sexo, rua=cliente.rua,
                           numero=cliente.numero, complemento=cliente.complemento, bairro=cliente.bairro,
                           cidade=cliente.cidade, pais=cliente.pais)


def mostrar_cliente_id(pk):
    cliente = Cliente.objects.get(id=pk)
    return cliente


def remover_cliente(cliente):
    cliente.delete()


def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.data_nascimento = cliente_novo.data_nascimento
    cliente.email = cliente_novo.email
    cliente.profissao = cliente_novo.profissao
    cliente.sexo = cliente_novo.sexo
    cliente.rua = cliente_novo.rua
    cliente.numero = cliente_novo.numero
    cliente.complemento = cliente_novo.complemento
    cliente.bairro = cliente_novo.bairro
    cliente.cidade = cliente_novo.cidade
    cliente.pais = cliente_novo.pais
    cliente.save(force_update=True)
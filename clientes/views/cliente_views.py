from django.shortcuts import render, redirect
from clientes.services import cliente_service
from clientes.forms.cliente_form import ClienteForm
from clientes.entidades import cliente


def listar_todos_clientes(request):
    clientes = cliente_service.listar_todos_clientes()

    return render(request, 'clientes/listar_todos_clientes.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            email = form_cliente.cleaned_data["email"]
            profissao = form_cliente.cleaned_data["profissao"]
            sexo = form_cliente.cleaned_data["sexo"]
            rua = form_cliente.cleaned_data["rua"]
            numero = form_cliente.cleaned_data["numero"]
            complemento = form_cliente.cleaned_data["complemento"]
            bairro = form_cliente.cleaned_data["bairro"]
            cidade = form_cliente.cleaned_data["cidade"]
            pais = form_cliente.cleaned_data["pais"]

            cliente_novo = cliente.Cliente(nome=nome, data_nascimento=data_nascimento, email=email,
                                           profissao=profissao, sexo=sexo, rua=rua, numero=numero,
                                           complemento=complemento, bairro=bairro, cidade=cidade, pais=pais)

            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('url_listar_todos_clientes')
    else:
        form_cliente = ClienteForm()

    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente})


def mostrar_cliente_id(request, pk):
    cliente = cliente_service.mostrar_cliente_id(pk)
    return render(request, 'clientes/mostrar_cliente_id.html', {'cliente': cliente})


def exluir_cliente(request, pk):
    cliente = cliente_service.mostrar_cliente_id(pk)
    if request.method == 'POST':
        cliente_service.remover_cliente(cliente)
        return redirect('url_listar_todos_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})


def editar_cliente(request, pk):
    cliente_antigo = cliente_service.mostrar_cliente_id(pk)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_antigo)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data["nome"]  # pega o atributo no input do formulario e salva em uma variavel
        data_nascimento = form_cliente.cleaned_data["data_nascimento"]
        email = form_cliente.cleaned_data["email"]
        profissao = form_cliente.cleaned_data["profissao"]
        sexo = form_cliente.cleaned_data["sexo"]
        rua = form_cliente.cleaned_data["rua"]
        numero = form_cliente.cleaned_data["numero"]
        complemento = form_cliente.cleaned_data["complemento"]
        bairro = form_cliente.cleaned_data["bairro"]
        cidade = form_cliente.cleaned_data["cidade"]
        pais = form_cliente.cleaned_data["pais"]

        cliente_novo = cliente.Cliente(nome=nome, data_nascimento=data_nascimento, email=email, profissao=profissao,
                                       sexo=sexo, rua=rua, numero=numero, complemento=complemento, bairro=bairro,
                                       cidade=cidade, pais=pais)

        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('url_listar_todos_clientes')
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente})
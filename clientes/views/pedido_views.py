from ..forms.pedido_form import PedidoForm
from django.shortcuts import render, redirect
from ..entidades import pedido
from ..services import pedido_service
from django.http import HttpRequest


def inserir_pedido(request):
    if request.method == "POST":
        form_pedido = PedidoForm(request.POST)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data["cliente"]
            data_pedido = form_pedido.cleaned_data["data_pedido"]
            valor = form_pedido.cleaned_data["valor"]
            status = form_pedido.cleaned_data["status"]
            observacoes = form_pedido.cleaned_data["observacoes"]
            produto = form_pedido.cleaned_data["produto"]

            pedido_novo = pedido.Pedido(cliente=cliente, data_pedido=data_pedido, valor=valor, status=status,
                                        observacoes=observacoes, produto=produto)

            pedido_service.cadastrar_pedidos(pedido_novo)
            return redirect('url_mostrar_pedidos')

    else:
        form_pedido = PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})


def mostrar_todos_pedidos(request):
    pedidos = pedido_service.mostrar_pedidos()
    return render(request, 'pedidos/mostrar_todos_pedidos.html', {"pedidos": pedidos})


def mostrar_pedido_id(request, pk):
    pedido = pedido_service.mostrar_pedido_id(pk)
    return render(request, 'pedidos/mostrar_pedido_id.html', {"pedido": pedido})


def editar_pedido(request, pk):
    pedido_antigo = pedido_service.mostrar_pedido_id(pk)
    form_pedido = PedidoForm(instance=pedido_antigo)
    if request.method == "POST":
        form_pedido = PedidoForm(request.POST, instance=pedido_antigo)
        if form_pedido.is_valid():
            cliente = form_pedido.cleaned_data["cliente"]
            data_pedido = form_pedido.cleaned_data["data_pedido"]
            valor = form_pedido.cleaned_data["valor"]
            status = form_pedido.cleaned_data["status"]
            observacoes = form_pedido.cleaned_data["observacoes"]
            produto = form_pedido.cleaned_data["produto"]

            pedido_novo = pedido.Pedido(cliente=cliente, data_pedido=data_pedido, valor=valor, status=status,
                                        observacoes=observacoes, produto=produto)

            pedido_service.editar_pedido(pedido_antigo, pedido_novo)
            return redirect('url_mostrar_pedidos')

    return render(request, 'pedidos/form_pedido.html', {"form_pedido": form_pedido})


def remover_pedido(request, pk):
    pedido = pedido_service.mostrar_pedido_id(pk)
    pedido_service.remover_pedido(pedido)

    return redirect('url_mostrar_pedidos')
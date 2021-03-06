from ..models import Pedido
from ..services import produto_service
from django.db import connection

def cadastrar_pedidos(pedido):
    pedido_bd = Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,
                                      status=pedido.status, observacoes=pedido.observacoes)
    pedido_bd.save()
    for i in pedido.produto:
        produto = produto_service.listar_produto_id(i.id)
        pedido_bd.produto.add(produto)


def mostrar_pedidos():
    pedidos = Pedido.objects.all()
    # pedidos = Pedido.objects.select_related('cliente').all()
    print(pedidos)
    # print(connection.queries)
    # print(len(connection.queries))
    return pedidos


def mostrar_pedido_id(pk):
    pedido = Pedido.objects.get(id=pk)
    return pedido


def editar_pedido(pedido, pedido_novo):
    pedido.cliente = pedido_novo.cliente
    pedido.data_pedido = pedido_novo.data_pedido
    pedido.valor = pedido_novo.valor
    pedido.status = pedido_novo.status
    pedido.observacoes = pedido_novo.observacoes
    pedido.produto.set(pedido_novo.produto)
    pedido.save(force_update=True)


def remover_pedido(pedido):
    pedido.delete()
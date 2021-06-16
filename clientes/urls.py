from django.urls import path
from clientes.views.cliente_views import listar_todos_clientes, cadastrar_cliente, mostrar_cliente_id, \
    exluir_cliente, editar_cliente

from clientes.views.pedido_views import inserir_pedido, mostrar_todos_pedidos, mostrar_pedido_id, editar_pedido,\
    remover_pedido

from clientes.views.produto_views import inserir_produto, listar_todos_produtos, remover_produto

urlpatterns = [
    path('', listar_todos_clientes, name='url_listar_todos_clientes'),
    path('cadastrar_cliente/', cadastrar_cliente, name='url_cadastrar_cliente'),
    path('mostrar_cliente/<int:pk>/', mostrar_cliente_id, name='url_mostrar_cliente'),
    path('remover_cliente/<int:pk>/', exluir_cliente, name='url_excluir_cliente'),
    path('editar_cliente/<int:pk>/', editar_cliente, name='url_editar_cliente'),

    #pedido urls
    path('cadastrar_pedido/', inserir_pedido, name="url_inserir_pedido"),
    path('mostrar_pedidos/', mostrar_todos_pedidos, name="url_mostrar_pedidos"),
    path('mostrar_pedido_id/<int:pk>/', mostrar_pedido_id, name="url_mostrar_pedido_id"),
    path('editar_pedido/<int:pk>/', editar_pedido, name="url_editar_pedido"),
    path('remover_pedido/<int:pk>/', remover_pedido, name="url_remover_pedido"),

    #produto urls
    path('cadastrar_produto/', inserir_produto, name="url_cadastrar_produto"),
    path('listar_todos_produtos/', listar_todos_produtos, name="url_listar_todos_produtos"),
    path('remover_produto/<int:pk>/', remover_produto, name="url_remover_produto")
]
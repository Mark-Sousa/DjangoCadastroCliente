from ..models import Produto


def listar_produto_id(id):
    produto = Produto.objects.get(id=id)
    return produto


def inserir_produto(produto):
    Produto.objects.create(nome=produto.nome, descricao=produto.descricao, valor=produto.valor)


def listar_todos_produtos():
    produto = Produto.objects.all()
    return produto


def remover_prod(produto):
    produto.delete()

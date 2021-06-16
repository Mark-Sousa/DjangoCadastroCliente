from ..forms.produto_form import ProdutoForm
from django.shortcuts import render, redirect
from ..services import produto_service
from ..entidades import produto


def inserir_produto(request):
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            nome = form_produto.cleaned_data["nome"]
            descricao = form_produto.cleaned_data["descricao"]
            valor = form_produto.cleaned_data["valor"]

            produto_novo = produto.Produto(nome=nome, descricao=descricao, valor=valor)
            produto_service.inserir_produto(produto_novo)
            return redirect('url_listar_todos_produtos')
    else:
        form_produto = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {"form_produto": form_produto})


def listar_todos_produtos(request):
    produtos = produto_service.listar_todos_produtos()
    return render(request, 'produtos/listar_todos_produtos.html', {"produtos": produtos})


def remover_produto(request, pk):
    prod = produto_service.listar_produto_id(pk)
    produto_service.remover_prod(prod)
    return redirect('url_listar_todos_produtos')
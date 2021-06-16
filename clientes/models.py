from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed


class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(null=False, blank=False, default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=False, blank=False)
    observacoes = models.CharField(max_length=50, null=True, blank=True)
    produto = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome


def pre_save_produto_receiver(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        produtos = instance.produto.all()
        tot = 0
        for i in produtos:
            tot += i.valor
        instance.valor = tot
        instance.save()


m2m_changed.connect(pre_save_produto_receiver, sender=Pedido.produto.through)


class Cliente(models.Model):
    SEXO_CHOICES = (
        ('M', "Masculino"),
        ('F', "Feminino"),
        ('N', "Nenhuma das opções")
    )

    nome = models.CharField(max_length=200, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    rua = models.CharField(max_length=200, default='', null=False, blank=False)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, default='', null=False, blank=False)
    bairro = models.CharField(max_length=50, default='', null=False, blank=False)
    cidade = models.CharField(max_length=50, default='', null=False, blank=False)
    pais = models.CharField(max_length=50, default='', null=False, blank=False)

    def __str__(self):
        return self.nome

# Generated by Django 3.2 on 2021-04-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 3.2 on 2021-04-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210428_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='observacoes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

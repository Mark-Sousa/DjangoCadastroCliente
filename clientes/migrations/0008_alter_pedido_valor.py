# Generated by Django 3.2 on 2021-05-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20210501_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
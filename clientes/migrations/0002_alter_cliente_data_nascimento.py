# Generated by Django 3.2 on 2021-04-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]

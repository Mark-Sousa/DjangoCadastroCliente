# Generated by Django 3.2 on 2021-04-23 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20210423_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='cliente',
            name='pais',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(default='', max_length=200),
        ),
    ]
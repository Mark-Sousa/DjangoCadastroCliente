# Generated by Django 3.2 on 2021-04-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profissao', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminono'), ('N', 'Nenhuma das opções')], max_length=1)),
            ],
        ),
    ]

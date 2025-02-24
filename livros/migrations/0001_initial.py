# Generated by Django 5.0.7 on 2025-02-16 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('quantidade_estoque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('quantidade_estoque', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=4)),
                ('id_categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.categorias')),
            ],
        ),
    ]

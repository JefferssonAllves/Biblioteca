# Generated by Django 5.0.7 on 2025-02-18 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_rename_id_categoria_livros_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='quantidade_estoque',
        ),
    ]

# Generated by Django 5.0.7 on 2025-02-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_rename_id_cliente_alugados_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alugados',
            name='devolvido',
            field=models.BooleanField(default=False),
        ),
    ]

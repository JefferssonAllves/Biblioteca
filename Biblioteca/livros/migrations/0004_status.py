# Generated by Django 5.0.7 on 2025-02-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_remove_livros_quantidade_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]

from django.db import models
from livros.models import Livros

class HistoricoAlugados(models.Model):
  id = models.AutoField(primary_key=True)
  id_cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
  id_livros = models.ForeignKey(Livros, on_delete=models.CASCADE)
  data_inicio = models.DateField()
  data_entrega = models.DateField(null=True)

  def __str__(self):
    return f'{self.id_cliente} - {self.id_livros}'

class Clientes(models.Model):
  id = models.AutoField(primary_key=True)
  cpf = models.CharField(max_length=14, unique=True)
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=100)
  telefone = models.CharField(max_length=15)
  email = models.EmailField()

  def __str__(self):
    return self.nome

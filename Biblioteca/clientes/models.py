from django.db import models
from livros.models import Livros
from django.contrib.auth.models import AbstractUser, Group, Permission


class Alugados(models.Model):
  id = models.AutoField(primary_key=True)
  cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
  livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
  data_inicio = models.DateField()
  data_entrega = models.DateField(null=True)
  devolvido = models.BooleanField(default=False)
  def __str__(self):
    return f'{self.cliente} - {self.livro}'

class Clientes(models.Model):
  id = models.AutoField(primary_key=True)
  cpf = models.CharField(max_length=14, unique=True)
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=100)
  telefone = models.CharField(max_length=15)
  email = models.EmailField()

  def __str__(self):
    return self.nome

class CustomUser(AbstractUser):
  cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)

  groups = models.ManyToManyField(
    Group,
    related_name="customuser_set",
    blank=True,
  )

  user_permissions = models.ManyToManyField(
    Permission,
    related_name="customuser_set",
    blank=True,
  )
  def __str__(self):
    return self.username

class Carrinho(models.Model):
  id = models.AutoField(primary_key=True)
  cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
  livro = models.ForeignKey(Livros, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.cliente} - {self.livro}'
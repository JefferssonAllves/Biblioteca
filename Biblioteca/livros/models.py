from django.db import models



class Categorias(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  quantidade_estoque = models.IntegerField()

  def __str__(self):
    return self.nome

class Imagens_Livros(models.Model):
  id = models.AutoField(primary_key=True)
  imagem = models.ImageField(upload_to="imagens_livros/")

  def __str__(self):
    return self.imagem


class Livros(models.Model):
  DISPONIVEL = 'Disponível'
  ALUGADO = 'Alugado'
  VENDIDO = 'Vendido'
  DEVOLVIDO = 'Devolvido'

  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=100)
  autor = models.CharField(max_length=100)
  ISBN = models.CharField(max_length=100)
  categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
  status = models.CharField(max_length=20)
  preco_alugar = models.DecimalField(max_digits=6, decimal_places=2)
  preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
  imagem = models.ForeignKey(Imagens_Livros, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.titulo
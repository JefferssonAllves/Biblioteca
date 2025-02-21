from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import Livros, Categorias
from math import ceil
from django.core import serializers
import json


# Create your views here.
def livros(request):
  if request.method == 'POST':
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    ISBN = request.POST.get('isbn')
    categoria = Categorias.objects.get(id=request.POST.get('categoria'))
    preco = float(request.POST.get('preco'))

    livro = Livros(titulo=titulo, autor=autor, ISBN=ISBN, status=Livros.DISPONIVEL, preco_venda=preco, categoria=categoria, preco_alugar=ceil(preco * 0.15))
    livro.save()

  livros = Livros.objects.all()
  return render(request, './livros.html', {'livros': livros, 'quantidade_disponivel': len(livros), 'categorias': Categorias.objects.all(), 'url_busca': reverse('livros_json'),})

def livro_update(request, id):
  try:
    if request.method == 'POST':
      titulo = request.POST.get('titulo')
      autor = request.POST.get('autor')
      ISBN = request.POST.get('ISBN')
      categoria = request.POST.get('categoria')
      preco = request.POST.get('preco_venda')
      status = request.POST.get('status')

      livro = Livros.objects.get(id=id)
      livro.titulo = titulo
      livro.autor = autor
      livro.ISBN = ISBN
      livro.status = status
      livro.preco_venda = preco
      livro.categoria = Categorias.objects.get(id=categoria)
      livro.preco_alugar = ceil(preco * 0.15)
      livro.save()
    livro = Livros.objects.get(id=id)
  except Exception as e:
    return redirect(reverse('livros'))
  return render(request, './livro_update.html', {'livro': livro, 'categorias': Categorias.objects.all(), })

def livro_delete(request):
  if request.method == 'POST':
    id = request.POST.get('livro_id')
    Livros.objects.filter(id=id).delete()
  return JsonResponse({'redirect': reverse('livros'), 'response': 200})

def categorias(request):
  if request.method == 'POST':
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')

    Categorias.objects.create(nome=nome, descricao=descricao, quantidade_estoque=0).save()
  categorias = Categorias.objects.all()
  return render(request, './categorias.html', {'categorias': categorias, 'quantidade_categorias': len(categorias)})

def categoria_update(request, id):
  try:
    if request.method == 'POST':
      nome = request.POST.get('nome')
      descricao = request.POST.get('descricao')
      categoria = Categorias.objects.get(id=id)
      categoria.nome = nome
      categoria.descricao = descricao
      categoria.save()
    categoria = Categorias.objects.get(id=id)
    livros_categoria = Livros.objects.filter(categoria=id)
  except Exception as e:
    return redirect(reverse('categorias'))
  return render(request, './categoria_update.html', {'categoria': categoria, 'livros': livros_categoria, 'quantidade_livros': len(livros_categoria)  })

def categoria_delete(request):
  if request.method == 'POST':
    id = request.POST.get('categoria_id')
    Categorias.objects.filter(id=id).delete()
  return JsonResponse({'redirect': reverse('categorias'), 'response': 200})

def livros_json(request): #TODO Arrumar para retornar todos os livros
  if request.META.get('HTTP_REFERER'):
    livros = json.loads(serializers.serialize('json',Livros.objects.all()))
    livros = [{'id': livro['pk'],
              'titulo': livro['fields']['titulo'],
              'autor': livro['fields']['autor'],
              'ISBN': livro['fields']['ISBN'],
              'categoria': Categorias.objects.get(id=livro['fields']['categoria']).nome,
              'preco_venda': livro['fields']['preco_venda'],
              'preco_alugar': livro['fields']['preco_alugar'],
              'status': livro['fields']['status'],} for livro in livros]
  else:
    livros = []
  return JsonResponse({'livros': livros})
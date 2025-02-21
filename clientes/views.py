from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import Clientes, Alugados
from difflib import get_close_matches
from livros.models import Livros, Categorias
from django.core import serializers
import json
from datetime import datetime, timedelta

def clientes(request):
  if request.method == 'POST':
    cpf = request.POST.get('cpf')
    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')

    try:
      Clientes(cpf=cpf, nome=nome, endereco=endereco, telefone=telefone, email=email).save()
      message = 'Cliente cadastrado com sucesso!'
    except Exception as e:
      return JsonResponse({'error': str(e)})

  clientes = Clientes.objects.all()
  return render(request, './clientes.html', {'clientes': clientes, 'total_clientes': len(clientes), 'url_busca': reverse('clientes_json')})

def cliente_update(request, id):
  try:
    if request.method == 'POST':
      cpf = request.POST.get('cpf')
      nome = request.POST.get('nome')
      endereco = request.POST.get('endereco')
      telefone = request.POST.get('telefone')
      email = request.POST.get('email')

      cliente = Clientes.objects.get(id=id)
      cliente.cpf = cpf
      cliente.nome = nome
      cliente.endereco = endereco
      cliente.telefone = telefone
      cliente.email = email
      cliente.save()

    cliente = Clientes.objects.get(id=id)
    alugados = Alugados.objects.filter(cliente=id)
    livros_alugados = []
    for livro in alugados:
      livros_alugados.append(Livros.objects.get(id=livro.livro.id))
  except Exception as e:
    return redirect(reverse('clientes'))
  return render(request, './cliente_update.html', {'cliente': cliente, 'livros': Livros.objects.all(), 'url_busca': reverse('livros_json'), 'livros_alugados': livros_alugados})

def cliente_delete(request):
  if request.method == 'POST':
    id = request.POST.get('cliente_id')
    Clientes.objects.filter(id=id).delete()
  return JsonResponse({'redirect': reverse('clientes')})

def alugar_livro(request, id):
  if request.method == 'POST':
    print(request.POST.get('livro_id'))
    livro = Livros.objects.get(id=request.POST.get('livro_id'))
    cliente = Clientes.objects.get(id=id)
    data_atual = datetime.now()
    data_futura = data_atual + timedelta(days=30)
    Alugados(cliente=cliente, livro=livro, data_inicio=data_atual, data_entrega=data_futura).save()

    livro.status = Livros.ALUGADO
    livro.save()
  return JsonResponse({'teste':'teste'})



def clientes_json(request):
  if request.META.get('HTTP_REFERER'):
    clientes = json.loads(serializers.serialize('json',Clientes.objects.all()))
    clientes = [
      {'id': cliente['pk'],
      'cpf': cliente['fields']['cpf'],
      'nome': cliente['fields']['nome'],
      'endereco': cliente['fields']['endereco'],
      'telefone': cliente['fields']['telefone'],
      'email': cliente['fields']['email']} for cliente in clientes]
  else:
    clientes = []
  return JsonResponse({'clientes': clientes})
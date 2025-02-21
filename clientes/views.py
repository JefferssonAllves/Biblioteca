from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import Clientes
from difflib import get_close_matches
from livros.models import Livros, Categorias
from django.core import serializers
import json
# Create your views here.
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
  except Exception as e:
    return redirect(reverse('clientes'))
  return render(request, './cliente_update.html', {'cliente': cliente, 'livros': Livros.objects.all()})

def cliente_delete(request):
  if request.method == 'POST':
    id = request.POST.get('cliente_id')
    Clientes.objects.filter(id=id).delete()
  return JsonResponse({'redirect': reverse('clientes')})

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
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from .models import Clientes, Alugados, Carrinho
from difflib import get_close_matches
from livros.models import Livros, Categorias
from django.core import serializers
import json
from datetime import datetime, timedelta
from django.contrib import messages
from .forms import CreateClienteUser

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

def register(request):
  if request.method == 'POST':
    form = CreateClienteUser(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Cadastro realizado com sucesso!')
      return redirect('login')  # Redireciona para a página de login após o registro
    else:
      form = CreateClienteUser()

    return render(request, 'accounts/register.html', {'form': form})
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
    livros_alugados = Alugados.objects.select_related('livro').filter(cliente=id) #TODO LINHA MUITO IMPORTANTE, RELACIONA TABELAS

  except Exception as e:
    return redirect(reverse('clientes'))
  return render(request, './cliente_update.html', {'cliente': cliente, 'livros': Livros.objects.filter(status=Livros.DISPONIVEL), 'url_busca': reverse('livros_json', args=[str(Livros.DISPONIVEL)]), 'livros_alugados': livros_alugados})

def cliente_delete(request):
  if request.method == 'POST':
    id = request.POST.get('cliente_id')
    Clientes.objects.filter(id=id).delete()
  return JsonResponse({'redirect': reverse('clientes')})

def alugar_livro(request, cliente_id):
  if request.method == 'POST':
    print(request.POST.get('livro_id'))
    livro = Livros.objects.get(id=request.POST.get('livro_id'))
    cliente = Clientes.objects.get(id=cliente_id)
    data_atual = datetime.now()
    data_futura = data_atual + timedelta(days=30)
    Alugados(cliente=cliente, livro=livro, data_inicio=data_atual, data_entrega=data_futura).save()

    livro.status = Livros.ALUGADO
    livro.save()
  return JsonResponse({'teste':'teste'})

def devolver_livro(request, id):
  if request.method == 'POST':
    emprestimo_id = request.POST.get('emprestimo_id')

    emprestimo = Alugados.objects.get(id=emprestimo_id)
    emprestimo.data_entrega = datetime.now()
    emprestimo.devolvido = True

    livro_emprestado = Livros.objects.get(id=emprestimo.livro.id)
    livro_emprestado.status = Livros.DISPONIVEL

    emprestimo.save()
    livro_emprestado.save()
  return JsonResponse({'redirect': 'etste'})

def add_livro_carrinho(request):
  if request.method == 'POST':
    livro_id = request.POST.get('livro_id')
    Carrinho.objects.create(livro_id=livro_id, cliente_id=16).save() #TODO LOGIN NECESSARIO

  return JsonResponse({'status': 'sucess'})
def rm_livro_carrinho(request):
  if request.method == 'POST':
    livro_id = request.POST.get('livro_id')
    Carrinho.objects.filter(livro_id=livro_id).delete()

  return JsonResponse({'status': 'sucess'})
def clientes_json(request): #TODO MELHORAR ESSA FORMA DE RETORNAR CLIENTES
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
from django.shortcuts import render
from livros.models import Livros, Categorias
from random import sample
# Create your views here.
def home(request):
  return render(request, './home.html', {'livros': Livros.objects.filter(status=Livros.DISPONIVEL), 'categorias': Categorias.objects.all()})
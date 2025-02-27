from django.shortcuts import render
from livros.models import Livros, Categorias
from random import sample
# Create your views here.
def home(request):
  categorias = sample(list(Categorias.objects.all()), 5)
  livros = Livros.objects.all()
  return render(request, './home.html', {'livros': Livros.objects.all(), 'categorias': categorias, 'livos': livros})
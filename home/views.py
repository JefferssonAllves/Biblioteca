from django.shortcuts import render
from livros.models import Livros
# Create your views here.
def home(request):
  return render(request, './home.html', {'livros': Livros.objects.all()})
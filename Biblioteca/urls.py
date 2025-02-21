
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('clientes/', include('clientes.urls')),
    path('livros/', include('livros.urls')),


]

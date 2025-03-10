
from django.urls import path
from . import views
urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('register/', views.register, name='register'),
    path('update/id=<int:id>/', views.cliente_update, name='cliente_update'),
    path('delete/', views.cliente_delete, name='cliente_delete'),

    path('add_livro_carrinho/', views.add_livro_carrinho, name='add_livro_carrinho'),
    path('rm_livro_carrinho/', views.rm_livro_carrinho, name='rm_livro_carrinho'),

    path('clientes_json/', views.clientes_json, name='clientes_json'),
    path('update/id=<int:cliente_id>/alugar_livro/', views.alugar_livro, name='alugar_livro'),
    path('update/id=<int:id>/devolver_livro/', views.devolver_livro, name='devolver_livro'),


]

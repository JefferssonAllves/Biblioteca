
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.clientes), name='clientes'),
    path('update/id=<int:id>/', login_required(views.cliente_update), name='cliente_update'),
    path('delete/', login_required(views.cliente_delete), name='cliente_delete'),

    path('cadastrar/', views.register, name='cadastrar_cliente'),
    path('login/', views.login, name='login_cliente'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('add_livro_carrinho/', login_required(views.add_livro_carrinho), name='add_livro_carrinho'),
    path('rm_livro_carrinho/', login_required(views.rm_livro_carrinho), name='rm_livro_carrinho'),

    path('clientes_json/', login_required(views.clientes_json), name='clientes_json'),
    path('update/id=<int:cliente_id>/alugar_livro/', login_required(views.alugar_livro), name='alugar_livro'),
    path('update/id=<int:id>/devolver_livro/', login_required(views.devolver_livro), name='devolver_livro'),

    path('teste/', views.teste, name='teste'),

]


from django.urls import path, include
from . import views
from clientes.views import devolver_livro
urlpatterns = [
    path('', views.livros, name='livros'),
    path('update/id=<int:id>/', views.livro_update, name='livro_update'),
    path('update/id=<int:id>/devolver_livro/', devolver_livro),

    path('delete/', views.livro_delete, name='livro_delete'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/update/id=<int:id>/', views.categoria_update, name='categoria_update'),
    path('categorias/delete/', views.categoria_delete, name='categoria_delete'),
    path('livros_json/filtro=<str:filtro>/', views.livros_json, name='livros_json'),

]

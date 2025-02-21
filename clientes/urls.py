
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('update/id=<int:id>/', views.cliente_update, name='cliente_update'),
    path('delete/', views.cliente_delete, name='cliente_delete'),
    path('clientes_json/', views.clientes_json, name='clientes_json'),
]

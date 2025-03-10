from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('clientes/', include('clientes.urls')),
    path('livros/', include('livros.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),

]

if settings.DEBUG: #TODO VER ARQUIVOS DE MEDIA ENVIADAS PELO USUARIO
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

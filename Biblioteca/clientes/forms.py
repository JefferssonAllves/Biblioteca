from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Clientes

class CreateClienteUser(UserCreationForm):
  nome = forms.CharField(max_length=255)
  cpf = forms.CharField(max_length=14)
  email = forms.EmailField(required=True)
  telefone = forms.CharField(max_length=15)
  endereco = forms.CharField(max_length=255)

  class Meta:
    model = CustomUser
    fields = ['username', 'email', 'nome', 'cpf', 'telefone', 'endereco', 'password1', 'password2']

    def save(self, commit=True):
      user = super().save(commit=False)
      cliente = Clientes(
        nome=self.cleaned_data['nome'],
        cpf=self.cleaned_data['cpf'],
        email=self.cleaned_data['email'],
        telefone=self.cleaned_data['telefone'],
        endereco=self.cleaned_data['endereco'],
      )
      if commit:
        cliente.save()
        user.cliente = cliente  # Associa o cliente ao usuário
        user.save()
      return user

from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('home/', login_required(views.home), name='home'),
]

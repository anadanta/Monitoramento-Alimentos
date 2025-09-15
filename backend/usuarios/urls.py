from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('sair', views.sair, name='sair'),
]

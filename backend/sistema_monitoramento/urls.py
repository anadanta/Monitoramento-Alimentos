from django.contrib import admin
from django.urls import path, include  

#urlpatterns = [
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('core.urls')),
    path('produtos/', include('produtos.urls')),
    path("", include('home.urls')),
    path("usuarios/", include('usuarios.urls')),
]
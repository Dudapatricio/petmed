"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from core.views import dashboard, cadastro_usuario, login_usuario
from consultas.views import consultas, nova_consulta, detalhes_consulta, editar_consulta
from Pets.views import petsCadastro, cadastrar_pet, editar_pet, detalhes_pet
from tutores.views import tutores, cadastrar_tutor, editar_tutor, detalhes_tutor

urlpatterns = [
    path('', cadastro_usuario, name='home'),  
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('consultas/', consultas, name='consultas'),
    path('consulta/nova/', nova_consulta, name='nova_consulta'),
    path('petsCadastro/', petsCadastro, name='petsCadastro'),
    path('pets/novo/', cadastrar_pet, name='cadastrar_pet'), 
    path('pets/editar/<int:pet_id>/', editar_pet, name='editar_pet'),
    path('tutores/', tutores, name='tutores'),
    path('tutores/novo/', cadastrar_tutor, name='cadastrar_tutor'),
    path('tutores/editar/<int:tutor_id>/', editar_tutor, name='editar_tutor'),
    path('pets/detalhes/<int:pet_id>/', detalhes_pet, name='detalhes_pet'),
    path('tutores/detalhes/<int:tutor_id>/', detalhes_tutor, name='detalhes_tutor'),
    path('consultas/detalhes/<int:consulta_id>/', detalhes_consulta, name='detalhes_consulta'),
    path('login/', login_usuario, name='login'),
    path('consultas/editar/<int:consulta_id>/', editar_consulta, name='editar_consulta'),
    path('dashboard/', dashboard, name='dashboard'),  
    path('cadastro/', cadastro_usuario, name='cadastro_usuario'),
]

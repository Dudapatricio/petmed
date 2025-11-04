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

from django.urls import path, include
from django.contrib import admin
from django.urls import path
from core.views import dashboard, consultas, petsCadastro, tutores, nova_consulta, cadastrar_pet, editar_pet, cadastrar_tutor, editar_tutor


urlpatterns = [
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
    
]

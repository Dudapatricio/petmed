# core/views.py
from django.shortcuts import render, redirect, get_object_or_404 
from consultas.models import Consulta
from tutores.models import Tutor
from Pets.models import Pet
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def dashboard(request):
    context = {
        'consultas_hoje': Consulta.objects.filter(data_consulta__date=date.today()).count(),
        'total_pets': Pet.objects.count(),
        'total_tutores': Tutor.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    
    return render(request, 'login.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'cadastro_usuario.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


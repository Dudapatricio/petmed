# core/views.py
from django.shortcuts import render, redirect, get_object_or_404 
from consultas.models import Consulta
from tutores.models import Tutor
from Pets.models import Pet
from datetime import date

def dashboard(request):
    context = {
        'consultas_hoje': Consulta.objects.filter(data_consulta__date=date.today()).count(),
        'total_pets': Pet.objects.count(),
        'total_tutores': Tutor.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from Pets.models import Pet
def consultas(request):
    consultas_list = Consulta.objects.all().order_by('-data_consulta')
    
    context = {
        'consultas': consultas_list,
        'total_consultas': consultas_list.count(),
        'confirmadas': consultas_list.filter(status='CONFIRMADA').count(),
        'pendentes': consultas_list.filter(status='AGENDADA').count(),
    }
    return render(request, 'consultas/consultas.html', context)

def nova_consulta(request):
    if request.method == 'POST':
        pet = Pet.objects.first()  
        Consulta.objects.create(
            pet=pet,
            veterinario=request.POST.get('veterinario', 'Dr. Teste'),
            data_consulta=request.POST.get('data_consulta'),
            status='AGENDADA'
        )
        return redirect('consultas')
    
    pets = Pet.objects.all()
    return render(request, 'consultas/nova_consulta.html', {'pets': pets})


def detalhes_consulta(request, consulta_id):
     consulta = get_object_or_404(Consulta, id=consulta_id)
     return render(request, 'consultas/detalhes_consulta.html', {
        'consulta': consulta
    })

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    
    if request.method == 'POST':
        consulta.pet_id = request.POST.get('pet')
        consulta.veterinario = request.POST.get('veterinario')
        consulta.data_consulta = request.POST.get('data_consulta')
        consulta.observacoes = request.POST.get('observacoes')
        consulta.sintomas = request.POST.get('sintomas')
        consulta.diagnostico = request.POST.get('diagnostico')
        consulta.medicamentos = request.POST.get('medicamentos')
        consulta.save()
        
        return redirect('consultas')

    pets = Pet.objects.all()
    return render(request, 'consultas/editar_consulta.html', {
        'consulta': consulta,
        'pets': pets
    })

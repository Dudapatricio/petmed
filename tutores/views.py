from django.shortcuts import render, redirect, get_object_or_404
from .models import Tutor
from Pets.models import Pet
def tutores(request):
    tutores_list = Tutor.objects.all()
    
    context = {
        'tutores': tutores_list,
        'total_tutores': tutores_list.count(),
        'tutores_ativos': tutores_list.filter(pets__isnull=False).distinct().count(),
    }
    return render(request, 'tutores/tutores.html', context)

def cadastrar_tutor(request):
    if request.method == 'POST':
       
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        cpf = request.POST.get('cpf')
        
        Tutor.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=endereco,
            cpf=cpf
        )
        return redirect('tutores')
    

    return render(request, 'tutores/cadastrar_tutor.html')

def editar_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    
    if request.method == 'POST':
        
        tutor.nome = request.POST.get('nome')
        tutor.telefone = request.POST.get('telefone')
        tutor.email = request.POST.get('email')
        tutor.endereco = request.POST.get('endereco')
        tutor.cpf = request.POST.get('cpf')
        tutor.save()
        return redirect('tutores')
    
    return render(request, 'tutores/cadastrar_tutor.html', {'tutor': tutor})

def detalhes_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    pets = Pet.objects.filter(tutor=tutor)
    return render(request, 'tutores/detalhes_tutor.html', {
        'tutor': tutor,
        'pets': pets
    })

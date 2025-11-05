# core/views.py
from django.shortcuts import render, redirect, get_object_or_404 
from dashboard.models import Pet, Tutor, Consulta
from datetime import date

def dashboard(request):
    context = {
        'consultas_hoje': Consulta.objects.filter(data_consulta__date=date.today()).count(),
        'total_pets': Pet.objects.count(),
        'total_tutores': Tutor.objects.count(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def consultas(request):
    consultas_list = Consulta.objects.all().order_by('-data_consulta')
    
    context = {
        'consultas': consultas_list,
        'total_consultas': consultas_list.count(),
        'confirmadas': consultas_list.filter(status='CONFIRMADA').count(),
        'pendentes': consultas_list.filter(status='AGENDADA').count(),
    }
    return render(request, 'core/consultas.html', context)

def petsCadastro(request):
    pets = Pet.objects.all()
    
    context = {
        'pets': pets,
        'total_pets': pets.count(),
        'total_cachorros': pets.filter(especie='CACHORRO').count(),
        'total_gatos': pets.filter(especie='GATO').count(),
        'total_outros': pets.exclude(especie__in=['CACHORRO', 'GATO']).count(),
    }
    return render(request, 'core/petsCadastro.html', context)

def tutores(request):
    tutores_list = Tutor.objects.all()
    
    context = {
        'tutores': tutores_list,
        'total_tutores': tutores_list.count(),
        'tutores_ativos': tutores_list.filter(pets__isnull=False).distinct().count(),
    }
    return render(request, 'core/tutores.html', context)

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
    return render(request, 'core/nova_consulta.html', {'pets': pets})



def cadastrar_pet(request):
    if request.method == 'POST':
        
        tutor_id = request.POST.get('tutor')
        nome = request.POST.get('nome')
        especie = request.POST.get('especie')
        raca = request.POST.get('raca')
        sexo = request.POST.get('sexo')
        data_nascimento = request.POST.get('data_nascimento')
        
        Pet.objects.create(
            tutor_id=tutor_id,
            nome=nome,
            especie=especie,
            raca=raca,
            sexo=sexo,
            data_nascimento=data_nascimento
        )
        return redirect('petsCadastro')
    
    
    tutores = Tutor.objects.all()
    return render(request, 'cadastrar_pet.html', {'tutores': tutores})

def editar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    if request.method == 'POST':
        
        pet.nome = request.POST.get('nome')
        pet.especie = request.POST.get('especie')
        pet.raca = request.POST.get('raca')
        pet.sexo = request.POST.get('sexo')
        pet.data_nascimento = request.POST.get('data_nascimento')
        pet.save()
        return redirect('petsCadastro')
    
    tutores = Tutor.objects.all()
    return render(request, 'cadastrar_pet.html', {'pet': pet, 'tutores': tutores})



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
    

    return render(request, 'cadastrar_tutor.html')

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
    
    return render(request, 'cadastrar_tutor.html', {'tutor': tutor})

def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    consultas = Consulta.objects.filter(pet=pet).order_by('-data_consulta')
    return render(request, 'core/detalhes_pet.html', {
    'pet': pet,
    'consultas': consultas
})

def detalhes_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    pets = Pet.objects.filter(tutor=tutor)
    return render(request, 'core/detalhes_tutor.html', {
        'tutor': tutor,
        'pets': pets
    })

def detalhes_consulta(request, consulta_id):
     consulta = get_object_or_404(Consulta, id=consulta_id)
     return render(request, 'core/detalhes_consulta.html', {
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
    return render(request, 'core/editar_consulta.html', {
        'consulta': consulta,
        'pets': pets
    })
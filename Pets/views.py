from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from tutores.models import Tutor
from consultas.models import Consulta

def petsCadastro(request):
    pets = Pet.objects.all()
    
    context = {
        'pets': pets,
        'total_pets': pets.count(),
        'total_cachorros': pets.filter(especie='CACHORRO').count(),
        'total_gatos': pets.filter(especie='GATO').count(),
        'total_outros': pets.exclude(especie__in=['CACHORRO', 'GATO']).count(),
    }
    return render(request, 'pets/petsCadastro.html', context)

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
    return render(request, 'pets/cadastrar_pet.html', {'tutores': tutores})

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
    return render(request, 'pets/cadastrar_pet.html', {'pet': pet, 'tutores': tutores})




def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    consultas = Consulta.objects.filter(pet=pet).order_by('-data_consulta')
    return render(request, 'pets/detalhes_pet.html', {
    'pet': pet,
    'consultas': consultas
})


# Create your views here.

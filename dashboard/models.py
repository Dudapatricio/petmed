from django.db import models
from datetime import date 

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.TextField(verbose_name="Endereço", blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, verbose_name="Observações")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

class Pet(models.Model):
    ESPECIE_CHOICES = [
        ('CACHORRO', 'Cachorro'),
        ('GATO', 'Gato'),
        ('ROEDOR', 'Roedor'),
        ('OUTRO', 'Outro'),
    ]

    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=15, choices=ESPECIE_CHOICES, default='CACHORRO')
    raca = models.CharField(max_length=30, verbose_name="Raça")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Peso em kg")
    cor = models.CharField(max_length=20, blank=True)
    observacoes = models.TextField(blank=True, verbose_name="Observações")

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='pets')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return "{} ({})".format(self.nome, self.raca)
    
    def idade(self):
        if self.data_nascimento:
            today = date.today()
            return today.year - self.data_nascimento.year - (
                (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
            )
        return None

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('CONFIRMADA', 'Confirmada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    veterinario = models.CharField(max_length=100)
    data_consulta = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='AGENDADA')
    sintomas = models.TextField(blank=True, verbose_name="Sintomas")
    diagnostico = models.TextField(blank=True, verbose_name="Diagnóstico")
    tratamento = models.TextField(blank=True, verbose_name="Tratamento")
    observacoes = models.TextField(blank=True, verbose_name='Observações')
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet.nome} - {self.data_consulta.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['-data_consulta']
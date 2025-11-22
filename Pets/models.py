from django.db import models
from datetime import date 
from tutores.models import Tutor


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

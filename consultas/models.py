from django.db import models
from Pets.models import Pet

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
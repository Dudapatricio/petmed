from django.db import models

# Create your models here.
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

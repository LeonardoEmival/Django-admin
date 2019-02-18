from django.db import models
from django.contrib import admin
class Curso(models.Model):
    nome = models.CharField(max_length= 30)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length= 100)
    valor = models.DecimalField(max_digits= 7, decimal_places=2)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

class Professor(models.Model):
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=12)
    valor_hora_aula = models.FloatField()

    def __str__(self):
        return self.nome



from django.db import models

class Colecao(models.Model):
    nome = models.CharField(max_length= 20)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    edicao = models.CharField()
    ano = models.IntegerField()

    def __str__(self):
        return self.ano

class Caixa(models.Model):
    numero = models.PositiveIntegerField()
    etiqueta = models.CharField(max_length= 20)
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.etiqueta

class Amigo(models.Model):
    nome = models.CharField(max_length=30)
    nome_mae = models.CharField(max_length=30)
    telefone = models.CharField(max_length=12)
    grupo_amigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolução = models.DateField()

    def __str__(self):
        return self.data_emprestimo

class Grupo_amigo(models.Model):
    PR = 'Predio'
    ES = 'Escola'
    YEAR_IN_Grupo_amigo_CHOICES = (
        (PR, 'Predio'),
        (ES , 'Escola'),

    )
    year_in_grupo_amigo = models.CharField(
        max_length=2,
        choices=YEAR_IN_Grupo_amigo_CHOICES,
        default=PR,
    )

    def is_upperclass(self):
        return self.year_in_grupo_amigo in (self.PR, self.ES)

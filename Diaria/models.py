from django.db import models

class Casa(models.Model):
    endereco = models.CharField(max_length= 20)
    valor_diaria = models.DecimalField(max_digits= 3, decimal_places= 2)
    tamanho = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Diaria(models.Model):
    data_diaria = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    valor_cobrado = models.DecimalField(max_digits= 3 , decimal_places= 2)

    def __str__(self):
        return self.data_diaria

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class ItemDiaria(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(max_length=100)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=30)
    numero = models.CharField(max_length= 6)
    complemento = models.CharField(max_length= 30)
    bairro = models.CharField(max_length= 20)
    cidade = models.CharField(max_length= 20)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.cidade

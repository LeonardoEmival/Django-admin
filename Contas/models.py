from django.db import models

class Contas(models.Model):
    data_criacao = models.DateField()
    tipo_despesa = models.CharField(max_length=20)
    descricao = models.TextField(max_length=60)
    forma_de_pagamento = models.CharField(max_length=30)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def __str__(self):
        return self.tipo_despesa

class Tipodespesa(models.Model):
        RE = 'Remedio'
        RO = 'Roupas'
        AL = 'Alimentação'
        ED = 'Educação'
        TR = 'Transporte'
        OU = 'Outros'
        YEAR_IN_Tipodespesa_CHOICES = (
            ( RE, 'Remedio'),
            (RO , 'Roupas'),
            (  ED , 'Educação'),
            ( TR ,'Transporte'),
            ( OU , 'Outros'),
        )
        year_in_tipodespesa = models.CharField(
            max_length=2,
            choices=YEAR_IN_Tipodespesa_CHOICES,
            default=RE,
        )

        def is_upperclass(self):
            return self.year_in_tipodespesa in (self.TR, self.OU)


class Forma_Pagamento(models.Model):
    DI = 'Dinheiro'
    CT = 'Cartão de Crédito'
    CD = 'Cartão de Débito'
    CC = 'Cartão Crediário'
    BL = 'Boleto'
    YEAR_IN_Forma_Pagamento_CHOICES = (
        (DI, 'Dinheiro'),
        (CT , 'Cartão de Crédito'),
        ( CD , 'Cartão de Débito'),
        (  BL , 'Boleto'),
    )
    year_in_forma_pagamento = models.CharField(
        max_length=2,
        choices=YEAR_IN_Forma_Pagamento_CHOICES,
        default=DI,
    )

    def is_upperclass(self):
        return self.year_in_forma_pagamento in (self.CC, self.BL)

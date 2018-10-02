import sys


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance):
        self.lances.append(lance)
        if lance.valor > self.maior_lance:
            self.maior_lance = lance.valor
        if lance.valor < self.menor_lance:
            self.menor_lance = lance.valor


class Usuario:

    def __init__(self, nome):
        self.nome = nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

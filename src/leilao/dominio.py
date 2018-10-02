class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.lances = []


class Usuario:

    def __init__(self, nome):
        self.nome = nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

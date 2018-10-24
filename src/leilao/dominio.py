import sys


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor: float):
        if self.carteira >= valor:
            self.carteira -= valor
            lance = Lance(self, valor)
            leilao.propoe(lance)
        else:
            raise ValueError('Nao pode dar lance maior que o valor da carteira')

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    @carteira.setter
    def carteira(self, valor):
        self.__carteira = valor


class Leilao:

    def __init__(self, descricao):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max
        self.descricao = descricao
        self.__lances = []

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('o mesmo usuário não pode dar o mesmo lance')

    @property
    def lances(self):
        return self.__lances[:]

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or self._diferente_do_ultimo_usuario(lance)

    def _tem_lances(self):
        return self.lances

    def _diferente_do_ultimo_usuario(self, lance):
        return self.lances[-1].usuario != lance.usuario

#
# class Avaliador:
#
#     def __init__(self):
#         self.maior_lance = sys.float_info.min
#         self.menor_lance = sys.float_info.max
#
#     def avalia(self, leilao):
#         for lance in leilao.lances:
#             if lance.valor > self.maior_lance:
#                 self.maior_lance = lance.valor
#             if lance.valor < self.menor_lance:
#                 self.menor_lance = lance.valor

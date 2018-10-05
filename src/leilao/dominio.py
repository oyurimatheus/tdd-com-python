from src.leilao.excecoes import LanceError


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    ERRO_MESMO_USUARIO = 'O mesmo usuario nao pode dar dois lances seguidos'

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.__maior_lance = 0
        self.__menor_lance = 0

    def propoe(self, lance):
        if self._lance_eh_valido(lance):

            if not self.lances:
                self.__menor_lance = lance.valor
            self.lances.append(lance)

            self.__maior_lance = lance.valor
        else:
            raise LanceError(self.ERRO_MESMO_USUARIO)

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or self._usuarios_diferentes(lance) and self._lance_eh_maior(lance)

    @property
    def lances(self):
        return self.__lances

    @property
    def maior_lance(self):
        return self.__maior_lance

    @maior_lance.setter
    def maior_lance(self, valor: float):
        self.__maior_lance = valor

    @property
    def menor_lance(self):
        return self.__menor_lance

    @menor_lance.setter
    def menor_lance(self, valor: float):
        self.__menor_lance = valor

    def _tem_lances(self):
        return self.lances

    def _usuarios_diferentes(self, lance):
        return self.lances[-1].usuario != lance.usuario

    def _lance_eh_maior(self, lance):
        return self.lances[-1].valor < lance.valor


class Usuario:

    ERRO_LANCE_MAIS_ALTO = 'Nao pode dar um lance com valor maior que a carteira'

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao: Leilao, valor: float):
        if valor <= self.carteira:
            self.carteira -= valor
            lance = Lance(self, valor)
            leilao.propoe(lance)
        else:
            raise ValueError(self.ERRO_LANCE_MAIS_ALTO)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def carteira(self):
        return self.__carteira

    @carteira.setter
    def carteira(self, valor):
        self.__carteira = valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

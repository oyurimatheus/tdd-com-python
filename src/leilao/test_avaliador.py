from unittest import TestCase

from src.leilao.dominio import Usuario, Leilao, Lance, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        leilao_celular = Leilao('Celular')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao_celular.lances.append(lance_do_yuri)
        leilao_celular.lances.append(lance_do_gui)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        avaliador = Avaliador()
        avaliador.avalia(leilao_celular)

        menor_lance_recebido = avaliador.menor_lance
        maior_lance_recebido = avaliador.maior_lance

        self.assertEqual(menor_lance_recebido, menor_lance_esperado)
        self.assertEqual(maior_lance_recebido, maior_lance_esperado)

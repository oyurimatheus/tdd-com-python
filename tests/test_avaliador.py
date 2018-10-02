from unittest import TestCase
from src.leilao.dominio import Leilao, Usuario, Lance, Avaliador


class TestAvaliador(TestCase):

    def test_avalia(self):
        # cria o cenario
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        leilao_celular = Leilao('Celular')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao_celular.lances.append(lance_do_yuri)
        leilao_celular.lances.append(lance_do_gui)

        # executa
        avaliador = Avaliador()
        avaliador.avalia(leilao_celular)

        self.assertEqual(avaliador.menor_lance, 100.0)
        self.assertEqual(avaliador.maior_lance, 200.0)

    def test_avalia1(self):
        # cria o cenario
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        leilao_celular = Leilao('Celular')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        leilao_celular.lances.append(lance_do_gui)
        leilao_celular.lances.append(lance_do_yuri)

        # executa
        avaliador = Avaliador()
        avaliador.avalia(leilao_celular)

        self.assertEqual(avaliador.menor_lance, 100.0)
        self.assertEqual(avaliador.maior_lance, 200.0)

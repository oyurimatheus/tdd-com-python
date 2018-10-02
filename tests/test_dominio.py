from unittest import TestCase
from src.leilao.dominio import Leilao, Usuario, Lance


class TestLeilao(TestCase):

    def setUp(self):
        # cria o cenario
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_lance_proposto_em_ordem_crescente(self):
        # executa

        self.lance_do_gui = Lance(self.gui, 200.0)
        self.lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(self.leilao.menor_lance, 100.0)
        self.assertEqual(self.leilao.maior_lance, 200.0)

    def test_deve_retornar_o_maior_e_o_menor_lance_proposto_em_ordem_decrescente(self):
        # executa

        self.lance_do_gui = Lance(self.gui, 200.0)
        self.lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual(self.leilao.menor_lance, 100.0)
        self.assertEqual(self.leilao.maior_lance, 200.0)

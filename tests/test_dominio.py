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

        lance_do_gui = Lance(self.gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_gui)

        self.assertEqual(self.leilao.menor_lance, 100.0)
        self.assertEqual(self.leilao.maior_lance, 200.0)

    def test_deve_retornar_o_maior_e_o_menor_lance_proposto_em_ordem_decrescente(self):
        # executa

        lance_do_gui = Lance(self.gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        self.assertEqual(self.leilao.menor_lance, 100.0)
        self.assertEqual(self.leilao.maior_lance, 200.0)

    def test_deve_permitir_propor_um_novo_lance_se_o_leilao_nao_tiver_lances(self):
        lance_do_gui = Lance(self.gui, 200.0)

        self.leilao.propoe(lance_do_gui)

        self.assertEqual(len(self.leilao.lances), 1)

    def test_deve_permitir_propor_um_novo_lance_se_o_ultimo_lance_nao_for_do_mesmo_usuario(self):
        lance_do_gui = Lance(self.gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 300.0)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        self.assertEqual(len(self.leilao.lances), 2)

    def test_deve_lancar_uma_excecao_se_o_ultimo_lance_for_do_mesmo_usuario(self):
        with self.assertRaises(ValueError):
            lance_do_gui = Lance(self.gui, 200.0)

            self.leilao.propoe(lance_do_gui)
            self.leilao.propoe(lance_do_gui)

            self.assertEqual(len(self.leilao.lances), 1)

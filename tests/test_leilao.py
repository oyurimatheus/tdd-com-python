from unittest import TestCase

from src.leilao.dominio import Leilao, Usuario, Lance
from src.leilao.excecoes import LanceError


class TestLeilao(TestCase):

    def setUp(self):
        # cria o cenario
        self.gui = Usuario('Gui', 300)
        self.yuri = Usuario('Yuri', 300)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_lance_proposto_em_ordem_crescente(self):
        # executa

        lance_do_yuri = Lance(self.yuri, 100.0)
        lance_do_gui = Lance(self.gui, 200.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_gui)

        menor_lance_devolvido = self.leilao.menor_lance
        maior_lance_devolvido = self.leilao.maior_lance

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        self.assertEqual(menor_lance_devolvido, menor_lance_esperado)
        self.assertEqual(maior_lance_devolvido, maior_lance_esperado)

    def test_deve_permitir_propor_um_novo_lance_se_o_leilao_nao_tiver_lances(self):
        lance_do_gui = Lance(self.gui, 200.0)

        self.leilao.propoe(lance_do_gui)

        total_de_lances_devolvido = len(self.leilao.lances)

        self.assertEqual(total_de_lances_devolvido, 1)

    def test_deve_permitir_propor_um_novo_lance_se_o_ultimo_lance_nao_for_do_mesmo_usuario(self):
        lance_do_gui = Lance(self.gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 300.0)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        total_de_lances_devolvido = len(self.leilao.lances)

        self.assertEqual(total_de_lances_devolvido, 2)

    def test_deve_lancar_uma_excecao_se_o_ultimo_lance_for_do_mesmo_usuario(self):
        with self.assertRaises(LanceError):
            lance_do_gui = Lance(self.gui, 200.0)

            self.leilao.propoe(lance_do_gui)
            self.leilao.propoe(lance_do_gui)

    def test_nao_deve_adicionar_lance_se_o_valor_for_menor_que_o_ultimo_lance(self):
        with self.assertRaises(LanceError):
            lance_do_yuri = Lance(self.yuri, 300.0)
            lance_do_gui = Lance(self.gui, 200.0)

            self.leilao.propoe(lance_do_yuri)
            self.leilao.propoe(lance_do_gui)

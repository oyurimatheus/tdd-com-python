from unittest import TestCase
from src.leilao.dominio import Leilao, Usuario, Lance

import pytest


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


def test_deve_mostrar_valor_da_carteira_de_um_usuario():
    yuri = Usuario('Yuri')
    gui = Usuario('Gui', 1000.0)

    assert yuri.carteira == 500.0
    assert gui.carteira == 1000.0


def test_deve_permitir_lance_de_usuario_com_valor_menor_do_que_o_da_carteira():
    leilao = Leilao('Celular')
    yuri = Usuario('Yuri')

    yuri.dar_lance(leilao, 100.0)

    assert len(leilao.lances) == 1


def test_deve_permitir_lance_de_usuario_com_valor_igual_ao_da_carteira():
    yuri = Usuario('Yuri')
    yuri.carteira = 100.0

    leilao = Leilao('Celular')

    yuri.dar_lance(leilao, 100.0)

    assert len(leilao.lances) == 1


def test_nao_deve_permitir_lance_de_usuario_com_valor_maior_que_o_da_carteira():
    with pytest.raises(ValueError):
        yuri = Usuario('Yuri', 100.0)
        leilao = Leilao('Celular')

        yuri.dar_lance(leilao, 500.0)

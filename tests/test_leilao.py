from unittest import TestCase

from src.leilao.dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):

    def setUp(self):
        self.yuri = Usuario('Yuri')

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_gui)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        menor_lance_recebido = self.leilao.menor_lance
        maior_lance_recebido = self.leilao.maior_lance

        self.assertEqual(menor_lance_esperado, menor_lance_recebido)
        self.assertEqual(maior_lance_esperado, maior_lance_recebido)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        menor_lance_recebido = self.leilao.menor_lance
        maior_lance_recebido = self.leilao.maior_lance

        self.assertEqual(menor_lance_esperado, menor_lance_recebido)
        self.assertEqual(maior_lance_esperado, maior_lance_recebido)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 100.0

        menor_lance_recebido = self.leilao.menor_lance
        maior_lance_recebido = self.leilao.maior_lance

        self.assertEqual(menor_lance_esperado, menor_lance_recebido)
        self.assertEqual(maior_lance_esperado, maior_lance_recebido)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)
        lance_do_yuri2 = Lance(self.yuri, 300.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri2)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 300.0

        menor_lance_recebido = self.leilao.menor_lance
        maior_lance_recebido = self.leilao.maior_lance

        self.assertEqual(maior_lance_esperado, maior_lance_recebido)
        self.assertEqual(menor_lance_esperado, menor_lance_recebido)

    def test_deve_permitir_propor_um_novo_lance_quando_o_leilao_nao_tiver_lances(self):
        lance_do_yuri = Lance(self.yuri, 200.0)

        self.leilao.propoe(lance_do_yuri)

        self.assertEquals(1, len(self.leilao.lances))

    def test_deve_permitir_propor_um_novo_lance_se_o_ultimo_lance_nao_for_do_mesmo_usuario(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 300.0)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_adicionar_lance_se_o_ultimo_lance_for_do_mesmo_usuario(self):
        lance_do_yuri = Lance(self.yuri, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_do_yuri)
            self.leilao.propoe(lance_do_yuri)

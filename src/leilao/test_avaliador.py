from unittest import TestCase

from src.leilao.dominio import Usuario, Leilao, Lance, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.yuri = Usuario('Yuri')

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(lance_do_gui)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_lance_recebido = avaliador.menor_lance
        maior_lance_recebido = avaliador.maior_lance

        self.assertEqual(menor_lance_recebido, menor_lance_esperado)
        self.assertEqual(maior_lance_recebido, maior_lance_esperado)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.lances.append(lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 200.0

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_lance_recebido = avaliador.menor_lance
        maior_lance_recebido = avaliador.maior_lance

        self.assertEqual(menor_lance_recebido, menor_lance_esperado)
        self.assertEqual(maior_lance_recebido, maior_lance_esperado)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_apenas_um_lance(self):
        lance_do_yuri = Lance(self.yuri, 100.0)

        self.leilao.lances.append(lance_do_yuri)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 100.0

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_lance_recebido = avaliador.menor_lance
        maior_lance_recebido = avaliador.maior_lance

        self.assertEqual(menor_lance_recebido, menor_lance_esperado)
        self.assertEqual(maior_lance_recebido, maior_lance_esperado)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        gui = Usuario('Gui')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(self.yuri, 100.0)
        lance_do_yuri2 = Lance(self.yuri, 300.0)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(lance_do_gui)
        self.leilao.lances.append(lance_do_yuri2)

        menor_lance_esperado = 100.0
        maior_lance_esperado = 300.0

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_lance_recebido = avaliador.menor_lance
        maior_lance_recebido = avaliador.maior_lance

        self.assertEqual(maior_lance_recebido, maior_lance_esperado)
        self.assertEqual(menor_lance_recebido, menor_lance_esperado)

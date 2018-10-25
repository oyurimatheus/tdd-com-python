from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalidoError


@pytest.fixture
def yuri():
    return Usuario('Yuri', 100)


def test_deve_subtrair_valor_da_carteira_ao_dar_um_lance(yuri):
    leilao = Leilao('Celular')
    yuri.propoe_lance(leilao, 50.0)

    assert yuri.carteira == 50.0


def test_deve_permitir_lance_de_usuario_com_valor_menor_do_que_o_da_carteira(yuri):
    leilao = Leilao('Celular')

    yuri.propoe_lance(leilao, 50.0)

    assert len(leilao.lances) == 1
    assert yuri.carteira == 50.0


def test_deve_permitir_lance_de_usuario_com_valor_igual_ao_da_carteira(yuri):
    leilao = Leilao('Celular')

    yuri.propoe_lance(leilao, 100.0)

    assert len(leilao.lances) == 1
    assert yuri.carteira == 0.0


def test_nao_deve_permitir_lance_de_usuario_com_valor_maior_que_o_da_carteira(yuri):

    with pytest.raises(LanceInvalidoError):
        leilao = Leilao('Celular')

        yuri.propoe_lance(leilao, 200.0)

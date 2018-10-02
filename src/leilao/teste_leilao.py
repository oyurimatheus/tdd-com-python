from src.leilao.dominio import Leilao, Usuario, Lance

gui = Usuario('Gui')
yuri = Usuario('Yuri')

leilao_celular = Leilao('Celular')

lance_do_gui = Lance(gui, 200.0)
lance_do_yuri = Lance(yuri, 100.0)

leilao_celular.lances.append(lance_do_gui)
leilao_celular.lances.append(lance_do_yuri)

for lance in leilao_celular.lances:
    print(f'Lance do usuario {lance.usuario.nome} com o valor de {lance.valor}')

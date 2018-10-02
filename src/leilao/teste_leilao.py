from src.leilao.dominio import Leilao, Usuario, Lance, Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')

leilao_celular = Leilao('Celular')

lance_do_gui = Lance(gui, 200.0)
lance_do_yuri = Lance(yuri, 100.0)

leilao_celular.lances.append(lance_do_yuri)
leilao_celular.lances.append(lance_do_gui)

for lance in leilao_celular.lances:
    print(f'Lance do usuario {lance.usuario.nome} com o valor de {lance.valor}')


avaliador = Avaliador()
avaliador.avalia(leilao_celular)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')
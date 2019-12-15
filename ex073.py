'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Atlético-PR', 'São Paulo',
         'Internacional', 'Corinthias', 'Bahia', 'Vasco da Gama', 'Góias',
         'Fortaleza', 'Atlético', 'Botafogo', 'Ceára SC', 'Cruzeiro', 'Fluminense',
         'CSA', 'Chapecoense', 'Avaí')
i = int(0)
print('-=' * 30)
print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os 5 primeiro são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times[16:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}º posição')
print('-=' * 30)

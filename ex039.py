#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

ano = int(input('Ano de nascimento: '))
now = datetime.now()
print('Quem nasceu em {} tem {} em {}'.format(ano, now.year - ano, now.year))
if now.year - ano < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - (now.year - ano)))
    print('Seu alistamento será em {}'.format(ano + 18))
elif now.year - ano > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(now.year - ano - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
else:
    print('Você deve se alistar imediatamente!')


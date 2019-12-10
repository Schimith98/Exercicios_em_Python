#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import datetime

ano = int(input('Ano de nascimento: '))
now = datetime.now()
print('O atleta tem {} anos'.format(now.year - ano))
if now.year - ano <= 9:
    print('Classificação: MIRIM')
elif now.year - ano <= 14:
    print('Classificação: INFANTIL')
elif now.year - ano <= 19:
    print('Classificação: JÚNIOR')
elif now.year - ano <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
maior = 0
menor = 0
now = datetime.now()
for i in range(1,8,1):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if now.year - ano >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
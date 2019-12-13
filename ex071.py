#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from math import floor
print('='*30)
print('BANCO CEV')
print('='*30)
valor = int(input('Que valor você quer sacar?'))

while True:
    if valor >= 50:
        print(f'Total de {floor(valor / 50)} cédulas de R$50')
        valor = valor % 50
    elif valor >= 20:
        print(f'Total de {floor(valor / 20)} cédulas de R$20')
        valor = valor % 20
    elif valor >= 10:
        print(f'Total de {floor(valor / 10)} cédulas de R$10')
        valor = valor % 10
    elif valor >= 1:
        print(f'Total de {valor} cédulas de R$1')
        valor = 0
    else:
        break

print('='*30)

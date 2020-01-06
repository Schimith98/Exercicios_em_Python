# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint

def maior(valores):
    print(f'{valores} foram informados {len(valores)} valores ao todo')
    if len(valores) == 0:
        print(f'O maior valor informado foi {max(valores)}')
    else:
        print(f'O maior valor informado foi {max(valores)}')
    print('-+'*15)


valores = []
fim = 6
j = 3
while fim >= 0:
    for i in range(0,fim):
        valores.append(randint(1, 10))
        '''if len(valores) == 0:
            valores.append((0))'''
    maior(valores)
    fim = j
    j -= 1
    valores.clear()

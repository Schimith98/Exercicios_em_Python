#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep

def contador(inicio, fim, passo):
    print('-='*15)
    print(f'Contagem de {inicio} até {fim} em {passo}: ')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(f'{i}', end=' ')
        print('FIM!')
    elif inicio > fim:
        for i in range(inicio, fim - 1, passo):
            sleep(0.5)
            print(f'{i}', end=' ')
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, -2)
INICIO = int(input('Início: '))
FIM = int(input('Fim: '))
PASSO = int(input('Passo:'))
if FIM < INICIO:
    PASSO *= -1

contador(INICIO, FIM, PASSO)
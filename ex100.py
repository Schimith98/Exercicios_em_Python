#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0,5):
        lista.append(randint(1,10))
    print(lista)


def somaPar(lista):
    soma = int(0)
    print(f'Somando os valores pares de {lista} temos', end=' ')
    for i in lista:
        if(i % 2 == 0):
            soma += i
    print(soma)


lista = list()
sorteia(lista)
somaPar(lista)

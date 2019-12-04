# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a
# sua porção Inteira.
from math import trunc

var = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(var, int(var)))

var = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(var, trunc(var)))


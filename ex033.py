#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro valor:'))
menor = n1
maior = n1

n2 = int(input('Segundo valor:'))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3 = int(input('Terceiro valor:'))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
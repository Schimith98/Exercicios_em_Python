#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número:'))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1
        print('\033[33m', i, end=' ')
    else:
        print('\033[31m', i, end=' ')

if cont == 2:
    print('\n\033[mO número {} foi divisível 2 vezes \nE por isso ele é PRIMO!'.format(num))
else:
    print('\n\033[mO número {} foi divisível {} vezes \nE por isso ele é NÃO é PRIMO!'.format(num, cont))



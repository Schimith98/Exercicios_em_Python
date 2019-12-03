#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

var = int(input('Digite um número inteiro para ver sua tabuada:'))
cont = 1;
print('-' * 12)
while cont < 11:
    print('{} x {} = {}'.format(var, cont, var*cont))
    cont = cont+1
print('-' * 12)



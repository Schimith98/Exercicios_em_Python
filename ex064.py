#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag).

n = 0
i = 0
cont = 0;
while i != 999:
    i = int(input('Digite um número [999 para parar]: '))
    if i != 999:
        n += i
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, n))

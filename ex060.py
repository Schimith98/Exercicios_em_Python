#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
print('Calculando {}! ='.format(num), end=' ')

while num > 0:
    fatorial *= num
    print('{}'.format(num), end=' ')
    if num > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    num = num - 1

print('{}'.format(fatorial))
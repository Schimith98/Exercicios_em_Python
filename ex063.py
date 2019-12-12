#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer mostrar? '))
i = 0
t1 = 0
t2 = 1
print('{} -> {} ->'.format(t1, t2), end=' ')
while i < n-2:

    f = t1 + t2
    print('{} ->'.format(f), end=' ')
    t1 = t2
    t2 = f
    i += 1

print('FIM')



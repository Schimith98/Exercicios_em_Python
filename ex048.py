#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

s = int(0)
for i in range(3, 501, 3):
    if i % 3 == 0:
        s += i
print('Valor da soma: {}'.format(s))

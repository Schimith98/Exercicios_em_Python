# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for c in range(0, 10):
    print('{}'.format(10-c))
    sleep(1)

print('-='*20)
print('FELIZ ANO NOVO!!')
print('-='*20)
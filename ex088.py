#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.
from random import randint
from time import sleep

jogo = list()
jogos = list()
i = 0
print('-'*30)
print('Joga na MEGA SENA')
print('-'*30)

cont = int(input('Quantos jogos você quer que eu sorteie?'))
print('Sorteando {cont} jogos:')
while i < cont:
    j = 0
    while j < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            j += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    print(f'Jogo {i+1}: {jogos[i]}')
    i += 1
    sleep(1)


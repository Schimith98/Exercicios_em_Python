#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
player = int(input('Qual é sua jogada?'))
if player >= 0 and player <= 2:

    pc = randint(0, 2)

    print('='* 30)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('=' * 30)

    if pc == 0:
        print('Computador jogou PEDRA'.format(pc))
    elif pc == 1:
        print('Computador jogou PAPEL'.format(pc))
    elif pc == 2:
        print('Computador jogou TESOURA'.format(pc))
    if player == 0:
        print('Jogador jogou PEDRA'.format(player))
    elif player == 1:
        print('Jogador jogou PAPEL'.format(player))
    elif player == 2:
        print('Jogador jogou TESOURA'.format(player))

    print('='* 10)

    if player == pc:
        print('EMPATE')
    elif (player == 0 and pc == 2) or (player == 1 and pc == 0) or (player == 2 and pc == 1):
        print('JOGADOR VENCE')
    else:
        print('O COMPUTADOR VENCEU')
else:
    print('Jogada inválida')


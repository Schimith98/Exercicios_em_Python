#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tentativas = 0
num_p1 = -1
num_pc = randint(0,11)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi? ')

while num_pc != num_p1:
    num_p1 = int(input('Qual seu palpite?'))
    tentativas += 1
    if(num_p1 < num_pc):
        print('Mais... Tente mais uma vez.')
    elif(num_p1 > num_pc):
        print('Menos.. Tente mais uma vez.')

print('Acertou com {} tentativas. GG WP'.format(tentativas))

#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:
    p1 = int(input('Diga um valor: '))
    p1PI = str(input('Par ou ímpar [P/I] ')).upper()
    print('-'*30)
    p2 = randint(0,10)
    print(f'Você jogou {p1} e o coputador {p2}. TOTAL DEU {p1+p2}', end=' ')
    if p1PI == 'P':
        if (p1+p2) % 2 == 0:
            print('PAR')
            print('-' * 30)
            print('Você GANHOU!')
            cont += 1
        else:
            break
    if p1PI == 'I':
        if (p1+p2) % 2 != 0:
            print('IMPAR')
            print('-'*30)
            print('Você GANHOU!')
        else:
            break
print(f'GAME OVER! Você venceu {cont} vezes.')
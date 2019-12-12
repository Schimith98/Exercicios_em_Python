#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

pt = int(input('Primeiro temo: '))
r = int(input('Razão: '))
i = 0
while i < 10:
    print(pt, end=' -> ')
    pt += r
    i += 1
print('ACABOU')
#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


pt = int(input('Primeiro temo: '))
r = int(input('Razão: '))
i = 0
x = 10
cont = 0

while i < x:
    print(pt, end=' -> ')
    cont += 1
    pt += r
    i += 1
    if i == x:
        print('PAUSA')
        x += int(input('Quantos termos você quer mostrar a mais?'))

print('Progressão finalizada com {} termos mostrados'.format(cont))
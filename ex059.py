'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
i = 4
while i != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    i = int(input('Qual a sua opção? '))

    #soma
    if i == 1:
        print('a soma entre {} + {} é {}'.format(valor1, valor2, valor1 + valor2))
    #multiplicar
    elif i == 2:
        print('a multiplicação entre {} x {} é {}'.format(valor1, valor2, valor1 * valor2))
    #maior
    elif i == 3:
        if valor1 > valor2:
            print('O primeiro valor {} é maior que o segundo valor {}.'.format(valor1, valor2))
        elif valor2 > valor1:
            print('O segundo valor {} é maior que o primeiro valor {}.'.format(valor2, valor1))
        else:
            print('Os valores {} e {} são iguais.'.format(valor1, valor2))
    #novos numeros
    elif i == 4:
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))

#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    else:
        for i in range(1, 11, 1):
            print(f'{num} x {i} = {num*i}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
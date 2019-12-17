'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
valores_pares = 0
soma_terceira_coluna = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))

print('=--='*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=--='*15)
maior_segunda_linha = matriz[1][0]
for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            valores_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        if linha == 1:
            if maior_segunda_linha < matriz[linha][coluna]:
                maior_segunda_linha = matriz[linha][coluna]

print(f'A soma dos valores pares é {valores_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')



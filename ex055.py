# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.

menor = float(0)
maior = float(0)

for i in range(1, 5 + 1, 1):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if menor == 0 and maior == 0:  # iniciando as variaveis
        menor = peso
        maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso lido foi de {:.2f}Kg'.format(maior))
print('O menor peso lido foi de {:.2f}Kg'.format(menor))



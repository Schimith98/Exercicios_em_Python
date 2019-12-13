'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total_gasto = 0
cont_maisq_1000 = 0
barato_nome = 'x'
barato = 0

print('*'*30)
print('LOJAS SUPER BARATÃO')
print('*'*30)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if total_gasto == 0:
        barato = preco
    if preco > 1000:
        cont_maisq_1000 += 1
    if barato >= preco:
        barato = preco
        barato_nome = nome
    total_gasto += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print(f'O total da compra foi R${total_gasto}')
print(f'Temos {cont_maisq_1000} produto(s) custando mais que R$1000,00 ')
print(f'O Produto mais barato foi {barato_nome} que custa {barato}' )

#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

i = 'x'
cont = 0
maior = 0
menor = 0
media = 0

while i != 'n':
    num = int(input('Digite um número: '))
    if i == 'x':
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    media += num
    cont += 1
    i = str(input('Quer continuar? [S/N] ')).lower()

media = media / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


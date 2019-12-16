'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
cont = int(0)
while True:
    lista.append(int(input('Digite um valor:')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar in 'Nn':
        break

print(f'Foram digitados {cont} números')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')

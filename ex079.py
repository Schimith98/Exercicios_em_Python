#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = list()
num = int
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucessso...')
    a = str(input(('Quer continuar?[S/N] '))).upper()
    if a in 'Nn':
        break
lista.sort()
print(f'Os valores digitados foram: {lista}')


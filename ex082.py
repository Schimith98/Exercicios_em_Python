#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.

list1 = list()
pares = list()
impares = list()
i = int()
while True:
    list1.append(int(input('Digite um valor: ')))
    if list1[i] % 2 == 0:
        pares.append(list1[i])
    else:
        impares.append(list1[i])
    i += 1
    resp = str(input('Quer continuar?[S/N] ')).upper()
    if resp in 'Nn':
        break
print(f'Lista: {list1}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
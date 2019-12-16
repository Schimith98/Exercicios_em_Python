#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for i in range(0,5):
    x = int(input('Digite um valor: '))
    if i == 0 or x > lista[- 1]:
        lista.append(x)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(lista)

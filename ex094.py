'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
lista = list()
media = 0
mulheres = list()
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: '))
        if dados['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Respoda M ou F.')
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    lista.append(dados.copy())
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn' or 'Ss':
            break
        else:
            print('ERRO! Respoda S ou N.')
    if resp in 'Nn':
        break
print('-=' * 30)
media = media / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'Lista de pessoas que estão acima da média:')
for i in lista:
    if i['idade'] >= media:
        print(f'     Nome = {i["nome"]}; Sexo = {i["sexo"]}; Idade = {i["idade"]} ')
print('<< ENCERRADO >>')



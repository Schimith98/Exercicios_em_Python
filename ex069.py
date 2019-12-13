'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
 programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

cont_maior = 0
cont_homem = 0
cont_9vinha = 0
continuar = ''
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    p_idade = int(input('Idade:'))
    p_sexo = str(input('Sexo [M/F]: ')).upper()
    if p_idade > 18:
        cont_maior += 1
    if p_sexo == 'M':
        cont_homem += 1
    elif p_idade < 20:
        cont_9vinha += 1
    continuar = str(input('Quer Continuar? [S/N]')).upper()
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont_maior}')
print(f'Ao todo temos {cont_homem} homens cadastrados')
print(f'E temos {cont_9vinha} mulheres com menos de 20')
#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = float(0);
velho_idade = int(0)
velho_nome = str('')
cont9vinha = 0

for i in range(1, 4+1, 1):
    print('-'*5, '{}ª PESSOA'.format(i), '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()

    media += idade
    if sexo == 'M':
        if velho_idade < idade:
            velho_idade = idade
            velho_nome = nome

    if sexo == 'F':
        if idade < 20:
            cont9vinha += 1

media = media / 4
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho_idade, velho_nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont9vinha))

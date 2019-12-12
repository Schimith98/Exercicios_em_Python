#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.

sexo = str('X')

while sexo != 'M' and sexo != 'F':
    sexo = str(input('É menino[M] ou menina[F]? ')).strip().upper()


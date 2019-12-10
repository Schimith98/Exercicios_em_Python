#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO

n1 = float(input('Primeiro nota:'))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
print('A média é {} e o aluno está:'.format(media))
if media >= 5:
    print('APROVADO!')
else:
    print('REPROVADO')

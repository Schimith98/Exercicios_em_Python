#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

boletim = list()
notas = list()
cont = 0
while True:
    notas.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    notas.append(cont)
    cont += 1
    media = (notas[1] + notas[2]) / 2
    notas.append(media)
    boletim.append(notas[:])
    notas.clear()
    resp = str(input('Quer continuar?[S/N]'))
    if resp in 'Nn':
        break
cont = 0
print('-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i in boletim:
    print(f'{cont:<4}{i[0]:<10}{i[4]:>8.1f}')
    cont += 1;
print('-'*30)

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if aluno == 999:
        break
    elif aluno == boletim[aluno][3]:
        print(f'As notas de {boletim[aluno][0]} são {boletim[aluno][1]} e {boletim[aluno][2]}')





#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['nome'] = str(input('Nome:'))
dados['média'] = float(input('Média:'))
if dados['média'] >= 7:
    dados['situação'] = str('Aprovado')
else:
    dados['situação'] = str('Recuperação')
print('-'*30)

for k,v in dados.items():
    print(f'{k} é igual a {v}')

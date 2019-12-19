#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}
now = datetime.now()
dados['nome'] = str(input('Nome:'))
dados['idade'] = now.year - int(input('Ano de Nascimento:'))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem)'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = 60 - (now.year - dados['contratação'])
print('-='*15)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
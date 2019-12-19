#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()

dados['nome'] = str(input('Nome do jogador: '))
dados['partida'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()

for i in range(0, dados['partida']):
    dados['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
dados['total'] = sum(dados['gols'])
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {dados["partida"]} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'=>   Na partida {i+1}, fez {v}')
print(f'Foi um total de {dados["total"]} gols.')


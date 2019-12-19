#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
team = list()

while True:
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partida'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = list()
    for i in range(0, dados['partida']):
        dados['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    dados['total'] = sum(dados['gols'])
    team.append(dados.copy())

    resp = str(input('Quer continuar?'))
    if resp in 'Nn':
        break
print('-='*30)

print('Cod       nome              gols                total')
print('-'*60)
for i in range(0, len(team)):
    print(f'{(i):<10}{(team[i]["nome"]):<20}{str(team[i]["gols"]):<20}{str(team[i]["total"]):<20}')
print('-='*30)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if resp == 999:
        break
    else:
        print(f' --Levantamento do jogador {team[resp]["nome"]}: ')
        for i in range(0, len(team[resp]["gols"])):
            print(f'No jogo {i+1} fez {team[resp]["gols"][i]}')
#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual é a distancia da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dist))
valor = float(0)
if dist <= 200:
    valor = dist * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
else:
    valor = dist * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
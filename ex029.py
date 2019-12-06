#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v_carro = int(input('Qual a velocidade do carro?'))

if v_carro > 80:
    multa = float((v_carro - 80) * 7)
    print('MULTADO! Você excedeu o limite permitido de 80Km/h\nVocê deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um BOM DIA! Dirija com SEGURANÇA!')
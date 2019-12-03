#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

kmPercorrido = float(input('Quantos km rodados?'))
diasAlugados = float(input('Quantos dias alugados?'))
print('O total a pagar é de R${:.2f}'.format((diasAlugados * 60) + (kmPercorrido * 0.15)))


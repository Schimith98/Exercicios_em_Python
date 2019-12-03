#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.

var1 = float(input('Insira um valor em real para ser convertido em dolar: R$'))
var2 = float(input('Insira o preço de 1 dolar: $'))
print('R${:.2f} valem ${:.2f}'.format(var1, var1 / var2))

#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento? '))

prestacao_mensal = valor_casa / (anos_financiamento * 12)
salario_30 = salario_comprador * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, anos_financiamento, prestacao_mensal))
if salario_30 > prestacao_mensal:
    print('Empréstimo CONCEDIDO!')
elif salario_30 <= prestacao_mensal:
    print('Empréstimo NEGADO!')
#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('='*10, "LOJAS do LUQUINHAS", '='*10)
valor_inicial = float(input('Preço das compras: R$'))
valor_final = float(0)
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor_final = valor_inicial - (valor_inicial * 10 / 100)
elif opcao == 2:
    valor_final = valor_inicial - (valor_inicial * 5 / 100)
elif opcao == 3:
    valor_final = valor_inicial
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(valor_final / 2))
elif opcao == 4:
    valor_final = valor_inicial + (valor_inicial * 20 / 100)
    parcelas = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valor_final/parcelas))
else:
    valor_inicial = 0
    valor_final = 0
    print('Opção inválida')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_inicial, valor_final))

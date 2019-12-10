#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = float(peso/(altura * altura))
print('Seu IMC é {:.2f} e vc está '.format(imc), end="")
if imc < 18.5:
    print('abaixo do peso')
elif imc <= 25:
    print(' com o peso ideal')
elif imc <= 30:
    print('com sobrepeso')
elif imc <= 40:
    print('com obesidade')
else:
    print('com obesidade mórbida')
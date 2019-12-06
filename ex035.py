#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo

reta1 = float(input('Primeira segmento:'))
reta2 = float(input('Segunda segmento:'))
reta3 = float(input('Terceira segmento:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta2 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')
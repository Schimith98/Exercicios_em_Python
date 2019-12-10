#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

reta1 = float(input('Primeira segmento:'))
reta2 = float(input('Segunda segmento:'))
reta3 = float(input('Terceira segmento:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta2 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print('Os segmentos acima PODEM formar um triangulo EQUILATERO!')
    elif  reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Os segmentos acima PODEM formar um triangulo ISÓSCELES!')
    else:
        print('Os segmentos acima PODEM formar um triangulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo!')


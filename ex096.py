#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    return largura * comprimento


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
print(f'Area = {area(largura, comprimento)}')



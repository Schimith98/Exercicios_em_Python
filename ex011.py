#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

print('Área da parede: {}m²', format(largura*altura))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((largura*altura) / 2))

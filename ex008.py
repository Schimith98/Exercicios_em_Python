#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

var = float(input('Digite uma distância em metros:'))
print('A medida de {} corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(var, var/1000, var/100, var /10, var*10, var*100, var*1000))

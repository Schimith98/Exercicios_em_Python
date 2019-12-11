#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

pt = int(input('Primeiro temo: '))
r = int(input('Razão: '))

for i in range(0,10):
    print(pt, end=' -> ')
    pt += r
print('ACABOU')

#Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#OBS: TUPLAS SÂO IMUTÁVEIS
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezenove', 'vinte')
i = -1
while True:
    i = int(input('Digite um número de 0 a 20:'))
    if i <= 20 and i >= 0:
        print(f'Você digitou o número {tupla[i]}')
        break
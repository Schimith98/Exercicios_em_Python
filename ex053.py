#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
j = 0;
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

print(junto, inverso)
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')





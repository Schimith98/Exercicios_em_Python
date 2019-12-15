#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticar',
           'trabalhar', 'mercado', 'programador', 'futuro')

for i in range(0, len(palavras)):
    print(f'A palavra {palavras[i].upper()} possui as vogais:', end=' ')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in 'aeiou':
            print(palavras[i][j], end=' ')
    print('')



#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    tam = len(txt) + 4
    print('~'* tam)
    print(f'  {txt}  ')
    print('~' * tam)


escreva('Lucas Schimith')
escreva('Curso de Python no Youtube')
escreva('LSC')
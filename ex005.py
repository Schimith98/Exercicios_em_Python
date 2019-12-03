#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

var = int(input('Digite um número inteiro:'))
print('Seu antecessor é {} e seu sucessor é {}'.format(var-1,var+1))
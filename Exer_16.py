'''Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.'''
print()
from math import trunc# importe so a fução trunc da biblioteca math
numero = float(input('Digite um valor: ')) # variavel que recebe o número
print(f'O valor digitado é: {numero} e sua porção inteira é: {trunc(numero)}')
# uso a função trunc para pegar a primeira porção do número.
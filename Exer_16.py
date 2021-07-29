'''Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.'''
print()
import math # importei a biblioteca math
numero = float(input('Digite um valor: ')) # variavel que recebe o número
print(f'O valor digitado é: {numero} e sua porção inteira é: {math.trunc(numero)}')
# uso a função trunc para pegar a primeira porção do número.
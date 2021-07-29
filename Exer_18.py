'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor
 do seno, cosseno e tangente desse ângulo.'''
import math

print()
# import math # importei a bibiloteca math (biblioteca completa).
from math import radians, sin, cos, tan
angulo = float(input('Digite o valor de um ângulo qualquer: ')) # variavel que recebe o angulo
seno = sin(radians(angulo)) # variavel 2 que converte o seno para radiando
cosseno = cos(radians(angulo)) # variavel 3 que converte o cosseno para radiando
tangente = tan(radians(angulo)) # variavel 4 que converte o tangente para radiando
print(f'O angulo de {angulo:.2f}\ntem como SENO {seno:.2f}\nCOSSENO {cosseno:.2f}\nTANGENTE {tangente:.2f}')
'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
dos dígitos separados.'''
print()
num = int(input('Digite um número: '))
u = num // 1 % 10 # com esse calculo sempre pego o resto do numero. num / 1 * 10 /100 (unidade)
d = num // 10 % 10 # com esse calculo sempre pego o resto do numero. num / 10 * 10 /100 (dezena)
c = num // 100 % 10 # com esse calculo sempre pego o resto do numero. num / 100 * 10 /100 (centena)
m = num // 1000 % 10 # com esse calculo sempre pego o resto do numero. num / 1000 * 10 /100 (milhar)
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')



'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
print()
from  random import shuffle
nome01 = input('Digite o nome do primeiro aluno: ') # variavel 01
nome02 = input('Digite o nome do segundo aluno: ') # variavel 02
nome03 = input('Digite o nome do terceiro aluno: ') # variavel 03
nome04 = input('Digite o nome do quarto aluno: ') # variavel 04
lista = [nome01, nome02, nome03, nome04] # variavel lista
shuffle(lista) # embaralahamento do lista
print(f'A ordem dos alunos que vão apresentar o trabalho é: {lista}. ') # resultado da ordem do sorteio
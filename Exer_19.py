'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e
 escrevendo na tela o nome do escolhido.'''
print()
from random import choice # importei a biblioteca random e utilizei só o método choice
nome01 = input('Digite o nome do primeiro aluno: ') # variavel 01
nome02 = input('Digite o nome do segundo aluno: ') # variavel 02
nome03 = input('Digite o nome do terceiro aluno: ') # variavel 03
nome04 = input('Digite o nome do quarto aluno: ') # variavel 04
lista = [nome01, nome02, nome03, nome04] # foi criado uma variavel lista como os nomes informados dos alunos
escolhido = choice(lista) # foi criado uma variavel escolhido e aplicado o método choice dentro da lista
# o choice vai sortear um nome aleatorio dentro da variavel lista
print(f'O nome do aluno sorteado é: {escolhido}. ')

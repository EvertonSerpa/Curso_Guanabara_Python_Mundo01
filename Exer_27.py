'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
 o primeiro e o último nome separadamente.'''
print()
nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print('O seu primeiro nome: {}'.format(lista[0]))
print('O seu último nome: {}'.format(lista[len(lista)-1]))
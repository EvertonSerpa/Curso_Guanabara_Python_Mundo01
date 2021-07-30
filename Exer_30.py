'''Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.'''
print()
numero = int(input('Digite um número: '))
calculo = numero % 2 # na variavel calculo ele vai dar resto 0 ou 1 dependendo qual número o usuario digite. e com o if e else eu vou dizer quem vai ser par ou impar.
print()
if calculo == 0: # todo numero com resto 0 e é par
    print(f'O número {numero} é: PAR! ')

else: # todo o numero com resto 1 é ímpar.
    print(f'O número {numero} é ÍMPAR! ')
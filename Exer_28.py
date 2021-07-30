'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
 entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
print()
# import random # essa opção importa toda a biblioteca random
from random import randint # nessa opção só importo o randint da biblioteca random.
numero = int(input('Digite um número [0] até [5] '))
sorteio = randint(0,5) # randint gera um numero aleatorio entre 0 e 5
if numero == sorteio: # se meu numero for == ao numero sorteado, você ganha.
    print('VOCÊ GANHOU!!!')


else:
    print('O número sorteado foi: {} você escolheu o número: {}\nVOCÊ PERDEU!!!'.format(sorteio,numero))
# caso o número não for == ao sorteado você cai na outra condição, e perde.

# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
print()
num = int(input('Digite um número: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))

# Explicando o código
# Linha 3, foi criado a variavel num que recebe o valor digitado pelo usuário.
# Linha 4 a 13 foi criado print com a formatação de cada multiplicador.

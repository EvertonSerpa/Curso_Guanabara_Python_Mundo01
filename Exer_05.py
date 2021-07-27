# Exercício Python 5: Faça um programa que leia um número Inteiro e
# mostre na tela o seu sucessor e seu antecessor.

print()
num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1
print('Seu sucessor é {} e antecessor é: {}'.format(sucessor, antecessor))

# Explicando o código
# linha 5, é criada uma variavel que vai receber um número inteiro, informado pelo usuário.
# linha 6, é criada uma variavel que vai somar + 1 ao número informado pelo usuário, assim informado
# seu sucessor.
# linha 7, é criada uma variavel que vai diminuir - 1 ao número informado pelo usuário, assim informado
# # seu antecessor.
# linha 8, é criado o print informando o sucessor e antecessor com o .format.
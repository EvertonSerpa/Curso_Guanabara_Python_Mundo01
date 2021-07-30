'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

print()
nome = input('Digite o seu nome: ')
print()
ma = nome.upper() # upper coloca todas as letras em maiuscula
mi = nome.lower() # lower coloca todas as letras em minusculo
letras = nome.replace(' ','') # replace, retirei todos os espaços
conte = len(letras)# criei a variavel conte e usei len para contar as quantidades de letras
lista = nome.split() # trasnformei o nome informado pelo usuario em uma lista
letras_lista = len(lista[0]) # como transformei o nome em lista o primeiro nome fica com valor 0, então mandei
#contar a quantidade de letras da posição 0.

print(f'Seu nome em letras maiúsulas é: {ma}\nSeu nome em letras minúsculas é: {mi}\nA quantidade de letras do seu nome é: {conte}\nSeu primeiro nome tem {letras_lista} letras.')

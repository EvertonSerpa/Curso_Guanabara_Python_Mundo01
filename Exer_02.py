# Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma
# mensagem de boas-vindas.

nome = input('Qual o seu nome? ')
print('Você tem um belo nome! É um prazer te conhecer {}.'.format(nome))

#Comentários:
# Usei o print () na linha 3 para pular uma linha.
# Criei uma variável nome na linha 4 para solicitar que o usuário dígite um nome.
# No print linha 5 uma mensagem vai aparecer no final para o usúario
# usei o .format para colocar o nome digitado no campo print.
# lembrando que as {} chaves vai pegar dentro do .format o nome digitado pelo usúario.
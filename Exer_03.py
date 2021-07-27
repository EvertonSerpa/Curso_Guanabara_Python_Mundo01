# Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.
print()
num01 = float(input('Digite um número: '))
num02 = float(input('Digite outro número: '))
soma = num01+num02
print('A soma do número {:.1f} e {:.1f} é igual: {}'.format(num01,num02,soma))

# Explicando o código
# () → Parênteses. [] → Colchetes. {} → Chaves
# linha 2 inseri um print para inserir um espaço de uma linha.
# linha 3 criei a variavel (num01) que vai receber (armazenar) o valor digitado pelo usuario,
# usei o float para números não inteiros.
# linha 4 criei a variavel (num02) que vai receber (armazenar) o segundo valor digitado pelo usuario,
# # usei o float para números não inteiros..
# linha 5 criei uma variavel (soma) que vai somar os valores da variavel num01 e num02.
# linha 6 criei um print para imprimir na tela num01 e num02 mais a soma dos seus valores.
# {} usei as chaves para referir as variaveis que tinha criado anteriormente, usei o .format para especificar
# qual a ordem que as variaveis seria imprimida dentro do print.

#mini dicionário
# print = imprimi algo na tela desde que esteja fechado por '' simples ou "" dupla e entre parênteses ()
# num01, num02 e soma = variaveis para receber valores.
# float = estou especificando para aceitar valores não inteiros ex: 5.5 .
# input = comando que solicita que o usuário faça algo.
# o sinal de = nas linhas 3,4 e 5 significa que as variáveis criadas vão receber um valor(x)
# format = método de organização
# :.f1 = formatação das casas decimais que apareça na tela  :.f1 = 1 casa decimal :.f2 = duas casas decimais
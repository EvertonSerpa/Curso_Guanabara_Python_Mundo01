# Exercício Python 8: Escreva um programa que leia um valor em metros e o
# exiba convertido em centímetros e milímetros.
print('')
valor = float(input('Digite um valor em metros: '))
cent = valor * 100
mil = valor * 1000
print('O valor em metros é: {},\nconvertido para centímetros é: {:.1f}\nseu valor em milímetros é: {:.1f}'.format(valor,cent,mil))

# Explicando o código

# Linha 4, foi criada uma variavel valor que recebe um valor não inteiro digitado pelo usuário.
# Linha 5, foi criada a variavel cent para calcular o valor em centímetro, pegando o valor digitado no
# na variavel valor e multiplicando por 100.
# Linha 6, foi criada a variavel mil para calcular o valor em milímetros, pegando o valor digitado no
# na variavel valor e multiplicando por 1000.
# Linha 7, no print apresentei o valor digitado pelo usuário mais o valor convertido em centímetro e milímetros
# usei o .formt para organizar meu print.
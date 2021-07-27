# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.
print()
real = float(input('Digite quanto de dinheiro você tem na carteira R$: '))
dolar = real / 5.17 #valor do dolar em 27/07/2021#
print('Você pode comprar US$ {:.2f} dolar(s)'.format(dolar))

# Explicando o código.
# linha 4, foi criada uma variavel real que recebe o valor digitado pelo usuario.
# linha 5, foi criado uma variavel dolar que pega o valor de real e divide por 5.17 dando o valor que
# em dolar que a pessoa tem.
# linha 6, no print mostro o valor em dolares que a pessoa tem, usei o .format
'''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
print()
km = float(input('Informe a quantidade de Km percorrido: '))
dias = int(input('Informe a quantidade de dias: '))
calculando_dias = dias * 60
calculando_km = km * 0.15
print(f'A tarifa a ser paga pelos dias com o carro é: R$ {calculando_dias:.2f}\nA tarifa a ser paga pelos Km percorrido com o carro é: R$ {calculando_km:.2f}')
'''Explicando o código
Foi utilizado 4 variaveis
a primeira variavel recebe o valor em floar (não inteiro) informado pelo usuario.
a segunda variavel recebe o valor int (inteiro) informado pelo usuario.
a terceira variavel fas o calculo dos dias com o veiculo
a quarta variavel faz o calculo dos km percorrido com o veiculo.'''
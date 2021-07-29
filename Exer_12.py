'''Exercício Python 12: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.'''

print()
preco = float(input('Toda a loja está com 5% de desconto!\n\nInforme o preço do produto para receber o desconto R$ '))
desconto = preco - (preco * 5 / 100)
print(f'O valor do produto {preco:.2f}\ncom o desconto fica {desconto:.2f}')
'''Explicando o código
foi criado duas variaveis, a primeira recebe o valor do produto e a segunda faz o calculo da
% e subtrai do valor do produto, assim dando o valor com o desconto.'''
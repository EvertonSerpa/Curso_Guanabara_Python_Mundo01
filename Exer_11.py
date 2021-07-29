# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print()
print('Programa que calcula a largura e comprimento de uma aréa em METROS')
print()
largura = float(input('Informe a largura : '))
altura = float(input('Informe a altura: '))
area = largura * altura
tinta = area / 2
print(f'A largura é {largura:.2f}.\nA altura é {altura:.2f}.\nA aréa total é {area:.2f} metros quadrados.\nA quantidade de tinta necessária para pintar é: {tinta:.2f} litros.')
'''Explicando o código
foi criada três variaveis, 
largura recebe o valor digitado pelo usuario.
altura recebe o valor digitado pelo usuario.
area calcula a largura * altura.
tinta pega o valor da area e divide por 2'''''
'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''
print()
co = float(input('Comprimento do cateto oposto: ')) # Variavel que recebe o primeiro valor
ca = float(input('Comprimento do cateto adjacente: ')) # Variavel que recebe o segundo valor
hipotenusa = (co ** 2 + ca ** 2) ** (1/2) # Variavel que faz o calculo da hipotenusa
print(f'A hipotenusa vai ser: {hipotenusa:.2f}. ') # Print formatado
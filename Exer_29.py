'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
print()
velocidade = int(input('Informe a velocidade atual do veiculo: '))
print()
if velocidade > 80:
    multa = (velocidade-80) * 7
    print(f'Você foi multado por excesso de velocidade!\nValor da multa R$ {multa:.2f} ')

else:
    print('Você está dentro do limite de velocidade! ')
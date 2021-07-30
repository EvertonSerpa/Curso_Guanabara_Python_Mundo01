'''Exercício Python 25: Crie um programa que leia o nome de uma pessoa e
diga se ela tem “SILVA” no nome.'''
print()
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

''''
strip, retira os espaços a direita e esquerda do nome
pergunto se silva está dentro do nome com o comando silva in nome
e coloco todo o silva para maiusculo com o lower'''
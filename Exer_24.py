'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa
ou não com o nome “SANTO”.'''
print()
nome = str(input('Digite um nome: ')).strip() #retira os espaços com o comando strip
print(nome[:5].upper() == 'SANTO') # conto a quantidade de letras que tem santo, e transformo elas para upper
# deixo tudo maiusculo
'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas
 vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece
a última vez.'''
print()
frase = str(input('Digite uma frase no teclado: ')).upper().strip() # upper = converte todas letras pra maiusculas. striper = tira os espaços nas laterias direita e esquerda
print('A quantidade de vezes que a vogal a aparece é: {}'.format(frase.count('A'))) # O conut vai procurar quantas vogais A tem na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))# find vai procurar a 1 vogal a
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1)) # vai procurar a primeira vogal a apartir da direita


# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.
print()
v = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(v))
print('Só tem espaços?', v.isspace()) # pergunta se possui só espaços
print('É um número?' , v.isnumeric()) # se é um número
print('É alfabético?', v.isalpha()) # se é alfabetico
print('É alfanumérico?', v.isalnum()) # Se tem número e letras
print('Está em maiúscula?', v.isupper()) # Se está maiúsculo
print('Está em minúscula?', v.islower()) # Se está em minúsculo
print('Está capitalizada:', v.istitle()) # Primeria caractere esta em caixa alta

# o v = objeto que tem características e realiza funcionalidades, ele possui atributos e métodos.
# Os métodos são os que terminam em () parênteses
# Exercício Python 06: Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.
print()
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizquadrada = num ** (1/2)
print('O dobro do número: {} é {}, o triplo é {} e sua raiz quadrada é {:.1f}'.format(num, dobro, triplo, raizquadrada))

# Explicando o código
# linha 4 É criada a variavel num que vai receber o valor inteiro digitado pelo usuario.
# linha 5 É criada a variavel dobro que vai pegar o num e multiplicar por 2.
# linha 6 É criada a variavel triplo que vai pegar o num e multiplicar por 3.
# linha 7 É criada a variavel raizquadrada que vai pegar o num fazer a exponenciação.
# linha 8 É criado o print informando os dados solicitados pela questão. Usei o .formt para organizar o print.
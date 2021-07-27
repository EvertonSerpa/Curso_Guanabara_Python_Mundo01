# Exercício Python 7: Desenvolva um programa que leia as duas
# notas de um aluno, calcule e mostre a sua média.
print()
nota01 = float(input('Digite a primeira nota do aluno: '))
nota02 = float(input('Digite a segunda nota do aluno: '))
media = (nota01 + nota02) / 2
print('A primeira nota do aluno foi: {}\ne a segunda nota foi: {}\ntendo como média: {}'.format(nota01,nota02,media))

# Explicando o código
# Linha 4, a variavel nota01 vai receber o valor informado pelo usuário, o valor é não inteiro ja que a nota pode ser quebrada
# Linha 5, a variavel nota02 vai receber o valor informado pelo usuário, o valor é não inteiro ja que a nota pode ser quebrada
# Linha 6, é criada a variavel média que vai somar as duas notas informadas anteriormente e dividir por dois, dando a média do aluno
# Na linha 6 foi usado os () → Parênteses para forçar a soma primeiro e depois a divisão.
# Linha 7, informei as notas do aluno e sua média. \n é usado para quebrar linha
'''Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
 e mostre seu novo salário, com 15% de aumento.'''
print()
salario = float(input('informe o valor do seu salário R$ '))
calculando = salario + (salario * 15 /100)
print(f'O seu salário é R$ {salario:.2f}\ncom o reajuste fica R$ {calculando:.2f}')
'''Explicnado o código
Foi usado duas variaveis para a resolução da questão.
A primeira varivel recebe o valor so salario, que é informada pelo usuario
A segunda variavel faz o calculo
lembrando que no python temos ordem de precedente, então com as aspas () o python
 vai caular essa equação e depois vai fazer a soma'''
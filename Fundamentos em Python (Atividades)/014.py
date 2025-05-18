#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

#Entrada de dados

numero = int(input('Digite o valor desejado: '))

#lógica

if numero >= 0:
    print(f'O número {numero} é positivo')
else:
    print(f'O número {numero} é Negativo')

'''Correção

if numero > 0:
    print(f'O número {numero} é positivo')
elif numero == 0:
    print(f'O número {numero} é neutro')
else:
    print(f'O número {numero} é Negativo')
'''
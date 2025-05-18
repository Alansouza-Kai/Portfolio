#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

#Entrada de dados

numero = int(input('Digite o valor desejado: '))

#lógica

if numero %2==0:
    print(f'O número {numero} é Par')
else:
    print(f'O número {numero} é impar')

'''
método2


numero2 = input('Digite o valor desejado: ')

if numero2[-1] == '0': #o -1 serve para ser considerado o último dado do fatiamento.
    print('É Par')
elif numero2[-1] == '2':
    print('É Par')
elif numero2[-1] == '4':
    print('É Par')
elif numero2[-1] == '6':
    print('É Par')
elif numero2[-1] == '8':
    print('É Par')
else:
    print(f'O número {numero2} é impar')
'''
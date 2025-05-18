#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20

#entrada de dados
Numero = float(input('Digite o valor desejado: '))

#lógica

if Numero >=0 and Numero<= 10:
    print(f'O número {Numero} está entre 0 e 10')
elif Numero >10 and Numero<= 20:
    print(f'O número {Numero} está entre 10 e 20')
else:
    print(f'O número {Numero} é maior que 20')

'''
Correção

if  Numero > 20:
    print("maior que 20")
elif    Numero > 10:
    print("Entre 10 e 20")
elif    Numero > 0:
    print("Entre 0 e 10")
else:
    print("numero negativo")
'''




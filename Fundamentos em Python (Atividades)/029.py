#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.


n = int(input("Digite a tabuada desejada: "))

for i in range(1,11):
    tabuada = n * i
    print(f'{n}X{i}={tabuada}')

#correção

for i in range(1,11):
    print(f'{n}X{i}={n * i}')
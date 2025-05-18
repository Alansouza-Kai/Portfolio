#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

numero = int(input("Digite o número desejado: "))


for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
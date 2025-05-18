#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

n1 = 0
n2 = 1
contador = 0

numero = int(input("Escreva seu número: "))
print("------------------------------------")

while contador < numero:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    contador += 1


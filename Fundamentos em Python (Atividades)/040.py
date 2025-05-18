#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

N1 = 0
N2 = 1
N3 = None
Numero = None
Encerrar = 0


while Encerrar != Numero:
    Numero = int(input("Escreva seu Numero: "))
    print("------------------------------------")
    for i in range(0,Numero):
        N3 = N1 + N2
        print(N1)
        N1 = N2
        N2 = N3
        Encerrar = i+1

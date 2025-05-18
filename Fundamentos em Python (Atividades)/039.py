'''Faça um programa que leia um número e retorne o fatorial !
4! = 4 x 3 x 2 x 1
'''

final = None

while final != 0:
    N1 = int(input('Digite um número: '))
    for i in range(N1, 1, -1):
        N1 *= (i-1)
        print(N1)
    teste = input('Deseja continuar? [S/N]').strip().upper()[0]
    if  teste == "N":
        final = 0

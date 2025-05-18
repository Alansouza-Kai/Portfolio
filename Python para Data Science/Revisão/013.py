'''Faça um programa que leia um número e retorne o fatorial !
4! = 4 x 3 x 2 x 1  '''


numero = int(input("Digite um número inteiro: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}")
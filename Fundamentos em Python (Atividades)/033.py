#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

soma = 0
soma2 = 0

for i in range(1,501):
    if  i%4==0:
        soma = soma + i

print(soma)

#espaçamento
print("")

#metodo 2

for l in range(0,501,4):
    soma2 = soma2 + l

print(soma2)

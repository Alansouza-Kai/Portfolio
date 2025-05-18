#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

soma = 0
for i in range(1,11):
    valor = int(input("Escreva um número: "))
    if  valor %2==0:
        soma = soma + valor

print(f"A soma dos valores pares digitados é:{soma}")
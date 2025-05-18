#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

pesos = []

for i in range(7):
    peso = float(input("Digite o peso: "))
    pesos.append(peso)  # Adiciona o peso à lista

maior_peso = max(pesos)
menor_peso = min(pesos)

print("O maior peso lido foi:", maior_peso, "kg")
print("O menor peso lido foi:", menor_peso, "kg")
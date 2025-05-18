"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
"""

Nome = input("Escreva seu nome completo: ").strip()
Primeiro_nome = Nome.split()

print(Nome.upper())
print(Nome.lower())
print(len((Nome).replace(" ","")))
print(len(Primeiro_nome[0]))

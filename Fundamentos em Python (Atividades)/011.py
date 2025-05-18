#Crie um programa que leia o nome completo de uma pessoa e mostre:
'''
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''

#Entrada de dados
NomeCompleto = input("Digite seu nome completo: ").strip()

#busca de intervalo
fimnome = NomeCompleto.find(' ')
semespaco = NomeCompleto.replace(' ','')
Nome= NomeCompleto[:fimnome]

print(Nome)

#Saída de dados

print(f'Nome em maiúsculo: {NomeCompleto.upper()}'
      f'\nNome em Minusculo: {NomeCompleto.lower()}'
      f'\nQuantidade de letras = {len(semespaco)}'
      f'\nQuantas letras tem o primeiro nome = {len(Nome)}')

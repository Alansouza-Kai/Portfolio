'''Crie um programa que leia um nome, e mostre o primeiro e o último nome'''

#Entrada de dados
NomeCompleto = input("Digite seu nome completo: ").strip()

#busca de intervalo
nome = NomeCompleto.find(' ')
ultimosobrenome = NomeCompleto.rfind(' ')

#saída de dados

print(f'Primeiro nome: {NomeCompleto[:nome]}'
      f'\nÚltimo nome: {NomeCompleto[ultimosobrenome:].strip()}')
'''
#correção

primeiro_nome = NomeCompleto[:NomeCompleto.find(' ')]
Ultimo_nome = NomeCompleto[NomeCompleto.rfind(' ')+1:]

print(f'Primeiro nome: {primeiro_nome}'
      f'\nUltimo nome: {Ultimo_nome}')
'''
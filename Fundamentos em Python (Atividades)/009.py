#Escreva um programa que leia um tipo de dado e usando a função type(), retorne ao usuário, qual o tipo de dado informado

#Entrada de dado
dado = input('Digite o dado desejado: ')

#Verificação do tipo de dado (tá sempre retornando str, pois essa está sendo a entrada sem conversão)
tipo = type(dado)

#exibição de informações
print(f'O dado é: {tipo}')

#correção
print(type(dado))
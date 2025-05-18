#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

#Coleta de dados do usuário
nome = input('Digite o seu nome: ')
sobrenome = input('O seu Sobrenome: ')

#Contatenar dados
nome_completo = nome +' '+ sobrenome

#Saída de dados
print(f'Seu nome completo é:{nome_completo}')
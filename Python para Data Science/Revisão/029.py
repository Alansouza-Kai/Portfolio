#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

import random

Quantidade = int(input("Quantos jogos deseja fazer? "))
Lista_de_jogos = []
Lista_inicial = []


for i in range (Quantidade):
    while True:
        if len(Lista_de_jogos) == Quantidade:
            break
        else:
            while len(Lista_inicial) != 6:
                Lista_inicial.append(random.randint(1,60))
        Lista_de_jogos.append(Lista_inicial[:])
        Lista_inicial.clear()

print(Lista_de_jogos)

'''
for i in range (Quantidade):
    while True:
        if len(Lista_de_jogos) == Quantidade:
            break
        else:
            while len(Lista_inicial) != 6:
                valor = random.randint(1,60)
                if 
                Lista_inicial.append()
        Lista_de_jogos.append(Lista_inicial[:])
        Lista_inicial.clear()

print(Lista_de_jogos)
'''

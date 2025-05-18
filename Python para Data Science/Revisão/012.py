#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número.
#E no final, retorne também a quantidade de tentativas necessárias.

import random

numero = random.randint(1, 10)
tentativas = 0
chute = None

while chute != numero:
    chute = int(input("Seu palpite: "))
    tentativas += 1

print(f"Parabéns! Você acertou o número {numero} em {tentativas} tentativa(s).")
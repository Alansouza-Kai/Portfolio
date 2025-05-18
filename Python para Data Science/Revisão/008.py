#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

opcoes = ['pedra', 'papel', 'tesoura']

print("Escolha uma opção:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

jogador = int(input("Digite o número da sua escolha: "))
computador = random.randint(0, 2)

print(f"\nVocê escolheu: {opcoes[jogador]}")
print(f"O computador escolheu: {opcoes[computador]}")

resultado = (jogador - computador) % 3
mensagens = ["Empate!", "Você venceu!", "Computador venceu!"]

print(f"\nResultado: {mensagens[resultado]}")
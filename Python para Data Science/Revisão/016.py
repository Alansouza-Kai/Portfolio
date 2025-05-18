#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random

Vitorias = 0
Resultado = None

while True:
    PC = random.randint(1, 10)
    Escolha =  int(input("Vamos Jogar!!\n Digite o número de escolha desejada:\n1 - Par\n2 - Impar\naqui:  "))
    print("________________________________________")
    if  Escolha == 1:
        JGame = "Par"
    elif Escolha == 2:
        JGame = "Impar"
    else:
        print("Esse número não é válido")
        break
    Njogador = int(input("Agora digite um número de 0 à 10: "))
    print("________________________________________")
    Soma = PC + Njogador
    if Soma % 2 == 0:
        Resultado = "Par"
    else:
        Resultado = "Impar"
    if JGame == Resultado:
        Vitorias += 1
    else:
        break

print(f"Parabens, vê ganhou {Vitorias} vezes antes de perder")


#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random
PC = random.randint(1,10)
print(PC)
contador = 0
final = ''

while final != "acertou":
    print("Tente advinhar o número que estou pensando")
    resposta = int(input('Digite um número de 1 até 10: '))
    contador += 1
    if  resposta == PC:
        print(f'Você acertou, pensei no número {resposta}')
        final = "acertou"
        print(f'Você precisou de {contador} tentativas')
    else:
        print(f'Você errou')


#correção

j = int(input('digite algo entre 1 e 10: '))

contador = 1
while PC != j:
    j = int(input('digite algo entre 1 e 10: '))
    contador += 1

print(f'parabens!! acertou {PC} com {contador} vezes')
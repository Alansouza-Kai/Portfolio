#Escreva um programa que crie uma lista com varios números lidos pelo usuário, em seguida, exiba apenas os números ímpares da lista.
from sys import excepthook

Numeros = []
Impares = []
Continuar = "s"


while Continuar != "n":
    try:
        Numero = int(input("Digite o número desejado: "))
        if  Numero % 2 == 0:
            Numeros.append(Numero)
        else:
            Numeros.append(Numero)
            Impares.append(Numero)
    except:
        print("Apenas aceitamos números!!")
    Continuar = input("Deseja continuar? [S/N]").strip().lower()[0]

print(f"Os números impares digitados são os {Impares}")

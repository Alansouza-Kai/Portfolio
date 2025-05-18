#Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele digite um número negativo.
#Em seguida, exiba a lista na tela.

Lista = []
Valor = 0

while Valor >= 0:
    try:
        Valor = float(input("Digite seu número aqui: "))
        Lista.append(Valor)
    except:
        print("Apenas aceitamos números!!")

print(Lista)
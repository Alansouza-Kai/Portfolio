#Escreva um programa que tenha uma função, média(), que receba 5 parâmetros e retorne qual é a média

def média (a,b,c,d,e):
    return (a+b+c+d+e)/5

Valores = []

try:
    for i in range(5):
        Valor = float(input("Digite o peso: "))
        Valores.append(Valor)

    Resultado = média(*Valores)

    print(Resultado)
except:
    print("apenas aceitamos números")

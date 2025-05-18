#Escreva um programa que tenha uma função, maior(), que receba 5 parâmetros e retorne qual é o maior deles

def dados (a,b,c,d,e):
    print('-*-'*10)
    maximo = max(a,b,c,d,e)
    print(maximo)
    print('-*-'*10)

try:
    Valores = []
    for i in range(5):
        valor = float(input("Escreva seu número: "))
        Valores.append(valor)
    Resultado = dados(*Valores)
except:
    print("Apenas aceitamos números")
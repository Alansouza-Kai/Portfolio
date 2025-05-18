#Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno

def area(a,b):
    print('-*-'*10)
    valor = a * b
    print(valor)
    print('-*-' * 10)

try:
    altura = float(input("Digite a altura do muro: "))
    largura = float(input("Digite a largura do muro: "))
    area(altura,largura)
except:
    print("Apenas aceitanos múmeros")
#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''
Maximo = 0
Minimo = 99999999

for i in range(1,8):
    pesotemp = float(input("Escreva seu Peso: "))
    if  pesotemp > Maximo:
        Maximo = pesotemp
    elif Minimo == 99999999:
         Minimo = pesotemp
    else:
        if  pesotemp < Minimo:
            Minimo = pesotemp

print(f'O maior peso é de {Maximo} Kg, e o menor peso é de {Minimo} Kg')
'''
#correção "refinada"

maior_peso = None
menor_peso = None

for i in range(7):
    peso = float(input("Escreva seu Peso: "))

    if  menor_peso == None and maior_peso == None:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é de {maior_peso} K\n'
      f'O menor peso é de {menor_peso} Kg')
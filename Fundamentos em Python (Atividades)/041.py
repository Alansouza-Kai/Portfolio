#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

Menor = None
Maior = None
Encerrar = 'S'
media = 0
quantidadelida = 0

while Encerrar == 'S':
    Numero = int(input("Escreva seu Numero: "))
    if Menor == None and Maior == None:
        Maior = Numero
        Menor = Numero
        media = media + Numero
        quantidadelida += 1
        questao = input("Deseja escrever mais números? [S/N]").strip().upper()[0]
        if questao == 'N':
            Encerrar = 'N'

    elif Numero > Maior:
        Maior = Numero
        media += Numero
        quantidadelida += 1
        questao = input("Deseja escrever mais números? [S/N]").strip().upper()[0]
        if questao == "N":
            Encerrar = "N"

    elif Numero < Menor:
        Menor = Numero
        media += Numero
        quantidadelida += 1
        questao = input("Deseja escrever mais números? [S/N]").strip().upper()[0]
        if questao == "N":
            Encerrar = "N"
    else:
        media += Numero
        quantidadelida += 1
        questao = input("Deseja escrever mais números? [S/N]").strip().upper()[0]
        if questao == "N":
            Encerrar = "N"

print(f'O maior Numero é o {Maior}\n'
      f'O menor Numero é o {Menor}\n'
      f'A media dos números digitados é {media/quantidadelida}')
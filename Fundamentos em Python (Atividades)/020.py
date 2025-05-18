#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

# Estar em boas condições de saúde.
# Ter entre 16 e 69 anos, desde que a primeira doação tenha sido feita até 60 anos (menores de 18 anos, clique para ver documentos necessários e formulário de autorização).
# Pesar no mínimo 50kg.
# Estar descansado (ter dormido pelo menos 5 horas nas últimas 24 horas).
# Estar alimentado (evitar alimentação gordurosa nas 4 horas que antecedem a doação).

#entrada de dados

D1 = input('Você está bem de saúde? S/N ').lower().strip()
D2 = int(input('Qual a sua idade: '))
D3 = int(input('Qual o seu peso: '))
D4 = int(input('Quantas horas dormiu na última noite: '))
D5 = input('Você se alimentou hoje com comidas leves? S/N ').lower().strip()

#lógica

if D1 == 's' and D2 >= 16 and D2 <= 69 and D3 > 50 and D4 >= 5 and D5 == 's':
    print(f'Você pode doar sangue')
else:
    print(f'Você não pode doar sangue')

'''
Correção:

idade = int(input("Idade: "))
if idade > 16 and idade <69:
    peso = float(input("peso: "))
    if peso > 50:
        horas_sono = int(input("horas de sono: "))
        if horas_sono > 5:
            consumobebida = input("Bebeu nas ultimas 12 horas? [S/N]").strip().upper()[0]
            if consumobebida == "N":
                print("Pode doar")
            else:
                print("Não poderia beber")
        else:
            print("horas de sono insuficientes")
    else:
        print("Peso inapropriado")
else:
    print("Idade indevida")

'''

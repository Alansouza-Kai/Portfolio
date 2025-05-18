#Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número.
# No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.
#ZeroDivisionError ; ValueError


try:
    V1 = float(input("Digite o primeiro número: "))
    V2 = float(input("Digite o segundo número: "))
    Divisão = V1 / V2
    print(f'A divisão de {V1} por {V2} é igual à {Divisão}')
except ZeroDivisionError:
    print("Não é possível dividir por 0")
except ValueError:
    print("Utilize apenas números")
#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.)

#entrada de dados
D1 = int(input('Digite o dia desejado: '))

if  D1  == 1:
    print(f'o Dia {D1} é uma "Segunda feira"')
elif    D1 == 2:
    print(f'O dia {D1} é uma terça-feira')
elif    D1 == 3:
    print(f'O dia {D1} é uma quarta-feira')
elif    D1 == 4:
    print(f'O dia {D1} é uma quinta-feira')
elif    D1 == 5:
    print(f'O dia {D1} é uma sexta-feira')
elif    D1 == 6:
    print(f'O dia {D1} é uma sábado')
elif    D1 == 7:
    print(f'O dia {D1} é uma domingo')
else:
    print('Você digitou um número maior que 7')








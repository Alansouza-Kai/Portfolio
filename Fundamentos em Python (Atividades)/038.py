'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

operacao = 0

print('Para começarmos, digite 3 valores')

while operacao != 5:
    N1 = float(input("Digite o primeiro valor: "))
    N2 = float(input("Digite o Segundo valor: "))
    N3 = float(input("Digite o terceiro valor: "))
    operacao = int(input(f'Considerando as operações abaixo:\n'
                         f'1.Somar\n'
                         f'2.Multiplicar\n'
                         f'3.Maior\n'
                         f'4.Novos números\n'
                         f'5.Sair do programa\n'
                         f'Digite o número da opção desejada: '))
    if operacao == 1:
        print(f'A soma dos Número {N1} + {N2} + {N3} é igual à {N1+N2+N3}')
    elif operacao == 2:
        print(f'A mutiplicação dos Número {N1} * {N2} * {N3} é igual à {N1*N2*N3}')
    elif operacao == 3:
        if  N1 > N2 and N1 > N3:
            Maior = N1
        elif N2 > N1 and N2 > N3:
            Maior = N2
        else:
            Maior = N3
        print(f'O Maior número entre os valores {N1}, {N2}, {N3} é o {Maior}')
    elif operacao == 4:
        print(f'Vamos reiniciar então')
    elif operacao == 5:
        operacao = 5
        print(f'Obrigado por usar nossos seviços')
    else:
        print("Você digitou uma função inexistente")

#correção
'''
operacao = 0

print('Para começarmos, digite 3 valores')
N1 = float(input("Digite o primeiro valor: "))
N2 = float(input("Digite o Segundo valor: "))
N3 = float(input("Digite o terceiro valor: "))

while operacao != 5:
    operacao = int(input(f'Considerando as operações abaixo:\n'
                         f'1.Somar\n'
                         f'2.Multiplicar\n'
                         f'3.Maior\n'
                         f'4.Novos números\n'
                         f'5.Sair do programa\n'
                         f'Digite o número da opção desejada: '))
    if operacao == 1:
        print(f'A soma dos Número {N1} + {N2} + {N3} é igual à {N1+N2+N3}')
    elif operacao == 2:
        print(f'A mutiplicação dos Número {N1} * {N2} * {N3} é igual à {N1*N2*N3}')
    elif operacao == 3:
        if  N1 > N2 and N1 > N3:
            Maior = N1
        elif N2 > N1 and N2 > N3:
            Maior = N2
        else:
            Maior = N3
        print(f'O Maior número entre os valores {N1}, {N2}, {N3} é o {Maior}')
    elif operacao == 4:
        print(f'Vamos reiniciar então')
        N1 = float(input("Digite o primeiro valor: "))
        N2 = float(input("Digite o Segundo valor: "))
        N3 = float(input("Digite o terceiro valor: "))
    elif operacao == 5:
        operacao = 5
        print(f'Obrigado por usar nossos seviços')
    else:
        print("Você digitou uma função inexistente")
'''
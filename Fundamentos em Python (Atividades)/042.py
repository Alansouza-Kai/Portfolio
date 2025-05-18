#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair
"""
1 = Depósitos
2 = Saques
3 = Consulta de saldo
4 = Sair
"""
from platform import system_alias

Saldo = 0
Função = 0

print('Bem Vindo ao Banco Python')

while Função != 4:
    Função = int(input(f'Qual operação deseja efetuar hoje?\n'
                         f'1.Depositar\n'
                         f'2.Sacar\n'
                         f'3.Consultar Saldo\n'
                         f'4.Sair\n'
                         f'Digite o número da opção desejada: '))
    print("-------------------------------------")
    if Função == 1:
        Saldo += float(input("Quanto deseja depositar na conta hoje? "))
        print("-------------------------------------")
    elif Função == 2:
        Saldo -= float(input("Quanto sacar da conta? "))
        print("-------------------------------------")
    elif Função == 3:
        print(f'O Seu saldo atual é de {Saldo} Reais')
        print("-------------------------------------")
    elif Função == 4:
        print("Agradecemos pelo sua confiança em nossos serviços")
        print("-------------------------------------")
    else:
        print("Você digitou uma função inexistente")
        print("-------------------------------------")
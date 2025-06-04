#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

#Sacar: Permitir no máximo 3 saques diários, com limite máximo de 500 reais por saque. Caso não possua saldo, deve informar uma mensagem.
#Depósito: Permitir apenas valores positivos.
#mostrar todas as alterações feitas, e no final, o valor atual no formato R$xxx.xx

#atualização do desafio
# Estabelecer um limite de 10 transações diárias para uma conta
# Se tentar fazer uma transação após o limite, deve ser informado que foi excedido o limite do dia.
# Mostrar no extrato a data e hora das transações.
from datetime import datetime

def espacamento():
    print('--*--' * 10)

extrato = []
saldo_final = 0
saques = 0
transacoes = 0
limite_transacoes = 10

while True:
    try:
        resposta = int(input('''
Bem-vindo ao DioBank!!!
Qual operação deseja efetuar?
1. Depositar
2. Sacar
3. Extrato
4. Sair
Digite apenas o número da opção desejada: '''))
    except ValueError:
        espacamento()
        print("Erro!! Apenas aceitamos números.")
        espacamento()
        continue

    if resposta in [1, 2] and transacoes >= limite_transacoes:
        espacamento()
        print("Limite diário de 10 transações excedido! Tente novamente amanhã.")
        espacamento()
        continue

    if resposta == 1:
        espacamento()
        try:
            deposito = float(input('Quanto deseja depositar: '))
        except ValueError:
            espacamento()
            print("Por favor, apenas digite números positivos.")
            espacamento()
            continue

        if deposito <= 0:
            espacamento()
            print("Apenas aceitamos valores positivos, tente novamente!")
            espacamento()
            continue
        else:
            saldo_final += deposito
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append((data_hora, "Depósito", deposito))
            transacoes += 1
            espacamento()
            print(f"O valor de R${deposito:.2f} foi depositado na conta.")
            espacamento()

    elif resposta == 2:
        if saques >= 3:
            espacamento()
            print("Você já efetuou os 3 saques permitidos hoje.")
            espacamento()
            continue

        espacamento()
        try:
            saque = float(input('Quanto deseja sacar: '))
        except ValueError:
            espacamento()
            print("Por favor, apenas digite números positivos.")
            espacamento()
            continue

        if saque <= 0:
            espacamento()
            print("Apenas aceitamos valores positivos, tente novamente!")
            espacamento()
            continue

        if saque > saldo_final:
            espacamento()
            print("Você não possui saldo suficiente!")
            espacamento()
        elif saque > 500:
            espacamento()
            print("Apenas é permitido efetuar saques de no máximo R$500,00.")
            espacamento()
        else:
            saldo_final -= saque
            saques += 1
            transacoes += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append((data_hora, "Saque", -saque))
            espacamento()
            print(f"O valor de R${saque:.2f} foi sacado da conta.")
            espacamento()

    elif resposta == 3:
        espacamento()
        if not extrato:
            print("Não foram realizadas movimentações na conta.")
        else:
            for data, tipo, valor in extrato:
                if valor < 0:
                    print(f'{data} - {tipo} __________ R${abs(valor):.2f}')
                else:
                    print(f'{data} - {tipo} __________ R${valor:.2f}')
        espacamento()
        print(f'Seu saldo atual é R${saldo_final:.2f}.')
        espacamento()

    elif resposta == 4:
        espacamento()
        print("Obrigado por utilizar nossos serviços. Até logo!")
        espacamento()
        break

    else:
        espacamento()
        print("Opção inválida, tente novamente!")
        espacamento()

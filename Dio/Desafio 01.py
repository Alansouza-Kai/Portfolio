#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

#Sacar: Permitir no máximo 3 saques diários, com limite máximo de 500 reais por saque. Caso não possua saldo, deve informar uma mensagem.
#Depósito: Permitir apenas valores positivos.
#mostrar todas as alterações feitas, e no final, o valor atual no formato R$xxx.xx

def espaçamento():
    print('--*--'*10)

Extrato = []
Saldofinal = 0
saques = 0

while True:
    try:
        resposta = int(input('''
Bem vindo ao DioBank!!!
Qual operação deseja efetuar?
1.Depositar
2.Sacar
3.Extrato
4.Sair
Digite apenas o número da opção desejada: '''))
    except ValueError:
        espaçamento()
        print("Erro!! Apenas aceitamos números")
        espaçamento()
        continue


    if  resposta == 1:
        espaçamento()
        try:
            deposito = float(input('Quanto deseja depositar: '))
        except ValueError:
            espaçamento()
            print("Por favor, apenas digite números positivos")
            espaçamento()
            continue
        if deposito < 0:
            espaçamento()
            print("Apenas aceitamos valores positivos, tente novamente!!")
            espaçamento()
            continue
        else:
            Saldofinal += deposito
            Extrato.append(deposito)
            espaçamento()
            print(f"O Valor de R${deposito} foi depositado na conta")
            espaçamento()


    elif resposta == 2:
        if saques < 3:
            espaçamento()
            try:
                Saque = float(input('Quanto deseja Sacar: '))
            except ValueError:
                espaçamento()
                print("Por favor, apenas digite números positivos")
                espaçamento()
                continue
            if Saque < 0:
                espaçamento()
                print("Apenas aceitamos valores positivos, tente novamente!!")
                espaçamento()
                continue
            else:
                if Saque > Saldofinal:
                    espaçamento()
                    print('Você não possui saldo suficiente!!')
                    espaçamento()
                else:
                    if Saque > 500:
                        espaçamento()
                        print("Apenas é permitido efetuar saques de no máximo R$500.00")
                        espaçamento()
                    else:
                        Saldofinal -= Saque
                        Extrato.append(-1*Saque)
                        saques += 1
                        espaçamento()
                        print(f"O Valor de R${Saque} foi sacado da conta")
                        espaçamento()
        else:
            espaçamento()
            print("Você já efetuou o 3 saques limites de hoje")
            espaçamento()


    elif resposta == 3:
        espaçamento()
        for i in range(0,len(Extrato)):
            if Extrato[i] < 0:
                print(f'Saque _______________ R${Extrato[i]*-1:.2f}.')
            else:
                print(f'Depósito ____________ R${Extrato[i]:.2f}.')
        espaçamento()
        print(f'Seu Saldo atual é R${Saldofinal:.2f}.')
        espaçamento()


    elif resposta == 4:
        espaçamento()
        print("Obrigado por utilizar nossos serviços. Até logo!!")
        espaçamento()
        break


    else:
        espaçamento()
        print("Opção inválida, tente novamente!!!")
        espaçamento()


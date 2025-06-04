#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

#Sacar: Permitir no máximo 3 saques diários, com limite máximo de 500 reais por saque. Caso não possua saldo, deve informar uma mensagem.
#Depósito: Permitir apenas valores positivos.
#mostrar todas as alterações feitas, e no final, o valor atual no formato R$xxx.xx

#atualização do desafio:
'''Separar as ações existentes de saque, deposito e extrato, em funções.
Saque: Deve receber os argumentos apenas por nome (keyword only).

Depósito: A função depósito deve receber os argumentos apenas por posição (positional only).

Extrato : A função deve receber os argumentos por posição e nome.

Criar duas novas funções, cadastrar usuário (cliente), e Cadastrar conta corrente (vincular ela com usuário)

Criar usuário é composto por: Nome, Data de nascimento, CPF e endereço. O endereço é uma string com "Logradouro, Nro, bairro, cidade /sigla estado. Deve ser armazenado somente os números do CPF, ou seja, sem pontos e traços. Não podem ser cadastrados 2 usuários com o mesmo CPF.

Cria conta corrente: O programa deve armazenar contas em uma lista. Uma conta é composta por agência, numero da conta e usuário vinculado. O número da conta é sequencial iniciando em 1. A Agência é fixa ( 0001 ). Um usuário pode ter mais de uma conta, mas uma conta, só pode ter 1 usuário.

'''

from datetime import datetime


def espaçamento():
    print('--*--' * 10)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if usuario_existente:
        espaçamento()
        print("Já existe um usuário com esse CPF!")
        espaçamento()
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (Logradouro, Número, Bairro, Cidade/SiglaEstado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    espaçamento()
    print("Usuário criado com sucesso!")
    espaçamento()


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()

    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if usuario:
        print("\nConta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "cpf": cpf
        }
    else:
        espaçamento()
        print("Usuário não encontrado! Por favor, crie o usuário antes de criar a conta.")
        espaçamento()
        return None


def filtrar_conta(cpf, contas):
    contas_do_usuario = [conta for conta in contas if conta["cpf"] == cpf]
    if not contas_do_usuario:
        print("Nenhuma conta encontrada para este CPF.")
        return None

    print("Contas disponíveis:")
    for conta in contas_do_usuario:
        print(f'Agência: {conta["agencia"]} | Conta: {conta["numero_conta"]}')

    try:
        numero = int(input("Informe o número da conta que deseja acessar: "))
    except ValueError:
        print("Número inválido.")
        return None

    conta_selecionada = next(
        (conta for conta in contas_do_usuario if conta["numero_conta"] == numero), None)

    if not conta_selecionada:
        print("Conta não encontrada.")
        return None

    return conta_selecionada


def depositar(Saldofinal, Extrato, transacoes_diarias, /):
    if transacoes_diarias >= 10:
        espaçamento()
        print("Limite diário de 10 transações atingido!")
        espaçamento()
        return Saldofinal, transacoes_diarias

    espaçamento()
    try:
        deposito = float(input('Quanto deseja depositar: '))
    except ValueError:
        espaçamento()
        print("Por favor, apenas digite números positivos")
        espaçamento()
        return Saldofinal, transacoes_diarias

    if deposito < 0:
        espaçamento()
        print("Apenas aceitamos valores positivos, tente novamente!!")
        espaçamento()
    else:
        Saldofinal += deposito
        Extrato.append({
            "tipo": "Depósito",
            "valor": deposito,
            "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
        transacoes_diarias += 1
        espaçamento()
        print(f"O Valor de R${deposito} foi depositado na conta")
        espaçamento()

    return Saldofinal, transacoes_diarias


def sacar(*, Saldofinal, Extrato, saques, transacoes_diarias):
    if transacoes_diarias >= 10:
        espaçamento()
        print("Limite diário de 10 transações atingido!")
        espaçamento()
        return Saldofinal, saques, transacoes_diarias

    if saques >= 3:
        espaçamento()
        print("Você já efetuou os 3 saques permitidos de hoje")
        espaçamento()
        return Saldofinal, saques, transacoes_diarias

    espaçamento()
    try:
        Saque = float(input('Quanto deseja Sacar: '))
    except ValueError:
        espaçamento()
        print("Por favor, apenas digite números positivos")
        espaçamento()
        return Saldofinal, saques, transacoes_diarias

    if Saque < 0:
        espaçamento()
        print("Apenas aceitamos valores positivos, tente novamente!!")
        espaçamento()
    elif Saque > Saldofinal:
        espaçamento()
        print('Você não possui saldo suficiente!!')
        espaçamento()
    elif Saque > 500:
        espaçamento()
        print("Apenas é permitido efetuar saques de no máximo R$500.00")
        espaçamento()
    else:
        Saldofinal -= Saque
        Extrato.append({
            "tipo": "Saque",
            "valor": -Saque,
            "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
        saques += 1
        transacoes_diarias += 1
        espaçamento()
        print(f"O Valor de R${Saque} foi sacado da conta")
        espaçamento()

    return Saldofinal, saques, transacoes_diarias


def mostrar_extrato(Saldofinal, /, *, Extrato):
    espaçamento()
    if not Extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in Extrato:
            tipo = operacao['tipo']
            valor = operacao['valor']
            data = operacao['data']
            if tipo == 'Saque':
                print(f'{data} - {tipo:<15} R$ {abs(valor):.2f}')
            else:
                print(f'{data} - {tipo:<15} R$ {valor:.2f}')
    espaçamento()
    print(f'Seu Saldo atual é R$ {Saldofinal:.2f}')
    espaçamento()


# ==========================
# 🚀 PROGRAMA PRINCIPAL
# ==========================

AGENCIA = "0001"
usuarios = []
contas = []

saldos = {}
extratos = {}
saques_realizados = {}
transacoes_diarias = {}

numero_conta = 1

while True:
    try:
        opcao = int(input('''

Bem vindo ao DioBank!!!
Qual operação deseja efetuar?

1. Criar usuário
2. Criar conta corrente
3. Acessar conta (Depositar, Sacar, Extrato)
4. Sair

Digite apenas o número da opção desejada: '''))
    except ValueError:
        espaçamento()
        print("Erro!! Apenas aceitamos números")
        espaçamento()
        continue

    if opcao == 1:
        criar_usuario(usuarios)

    elif opcao == 2:
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
            cpf = conta["cpf"]
            saldos[(cpf, conta["numero_conta"])] = 0
            extratos[(cpf, conta["numero_conta"])] = []
            saques_realizados[(cpf, conta["numero_conta"])] = 0
            transacoes_diarias[(cpf, conta["numero_conta"])] = 0
            numero_conta += 1

    elif opcao == 3:
        cpf = input("Informe seu CPF: ").strip()

        conta = filtrar_conta(cpf, contas)
        if not conta:
            continue

        chave = (cpf, conta["numero_conta"])

        while True:
            try:
                operacao = int(input(f'''
Agência: {conta["agencia"]} | Conta: {conta["numero_conta"]}

Qual operação deseja realizar?
1. Depositar
2. Sacar
3. Extrato
4. Voltar ao menu anterior

Digite o número da operação: '''))
            except ValueError:
                espaçamento()
                print("Erro!! Apenas aceitamos números")
                espaçamento()
                continue

            if operacao == 1:
                saldo_atual, transacoes = depositar(
                    saldos[chave],
                    extratos[chave],
                    transacoes_diarias[chave]
                )
                saldos[chave] = saldo_atual
                transacoes_diarias[chave] = transacoes

            elif operacao == 2:
                saldo_atual, saques, transacoes = sacar(
                    Saldofinal=saldos[chave],
                    Extrato=extratos[chave],
                    saques=saques_realizados[chave],
                    transacoes_diarias=transacoes_diarias[chave]
                )
                saldos[chave] = saldo_atual
                saques_realizados[chave] = saques
                transacoes_diarias[chave] = transacoes

            elif operacao == 3:
                mostrar_extrato(
                    saldos[chave],
                    Extrato=extratos[chave]
                )

            elif operacao == 4:
                break

            else:
                espaçamento()
                print("Opção inválida, tente novamente!")
                espaçamento()

    elif opcao == 4:
        espaçamento()
        print("Obrigado por utilizar nossos serviços. Até logo!!")
        espaçamento()
        break

    else:
        espaçamento()
        print("Opção inválida, tente novamente!!!")
        espaçamento()

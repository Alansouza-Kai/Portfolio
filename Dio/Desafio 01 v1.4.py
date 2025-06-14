#Iniciar a modelagem do sistema bancário em POO. Adicionar classes para clientes e as operações bancárias: Depósito e Saque.
#Atualizar a implementação do sistema, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionarios. O Código deve seguir o modelo de Classes UML a seguir.


from datetime import datetime
import re

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo += self.valor
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta._saldo >= self.valor and conta._saques < 3 and conta._transacoes_diarias < 10 and self.valor <= 500:
            conta._saldo -= self.valor
            conta._saques += 1
            conta._transacoes_diarias += 1
            conta.historico.adicionar_transacao(self)
            return True
        return False


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })


class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self._saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self._cliente = cliente
        self.historico = Historico()
        self._saques = 0
        self._transacoes_diarias = 0

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        saque = Saque(valor)
        if saque.registrar(self):
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saque não realizado. Verifique o limite ou o número de saques.")

    def depositar(self, valor):
        if valor > 0:
            deposito = Deposito(valor)
            deposito.registrar(self)
            self._transacoes_diarias += 1
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def extrato(self):
        print("\n=== Extrato ===")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        for t in self.historico.transacoes:
            print(f"{t['data']} - {t['tipo']:<15} R$ {t['valor']:.2f}")
        print(f"\nSaldo atual: R$ {self._saldo:.2f}")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()


# Interface com input do usuário
if __name__ == "__main__":
    clientes = []
    contas = []

    def encontrar_cliente_por_cpf(cpf):
        return next((cliente for cliente in clientes if cliente.cpf == cpf), None)

    def input_cpf():
        while True:
            cpf = input("CPF (apenas números): ")
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            print("CPF inválido. Digite apenas números, sem pontos ou traços (11 dígitos).")

    def input_nascimento():
        while True:
            nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            try:
                datetime.strptime(nascimento, "%d/%m/%Y")
                return nascimento
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    def input_endereco():
        ufs_validas = {
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT",
            "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO",
            "RR", "SC", "SP", "SE", "TO"
        }
        padrao_geral = r'^(.+?),\s*(\d+.*?),\s*(.+?),\s*(.+?)\s*-\s*(\w{2})$'
        while True:
            endereco = input("Endereço (Rua, Número e complemento, Bairro, Cidade - UF): ")
            match = re.match(padrao_geral, endereco.strip(), re.IGNORECASE)
            if match:
                uf = match.group(5).upper()
                if uf in ufs_validas:
                    endereco_corrigido = f"{match.group(1)}, {match.group(2)}, {match.group(3)}, {match.group(4)} - {uf}"
                    return endereco_corrigido
            print("Endereço inválido. Use o formato correto: Rua, Número e complemento, Bairro, Cidade - UF (UF válida).")

    def criar_cliente():
        cpf = input_cpf()
        if encontrar_cliente_por_cpf(cpf):
            print("Cliente já cadastrado.")
            return
        nome = input("Nome: ")
        nascimento = input_nascimento()
        endereco = input_endereco()
        cliente = PessoaFisica(cpf, nome, nascimento, endereco)
        clientes.append(cliente)
        print("Cliente criado com sucesso!")

    def criar_conta():
        cpf = input_cpf()
        cliente = encontrar_cliente_por_cpf(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        print(f"Este cliente possui {len(cliente.contas)} conta(s).")
        criar = input("Deseja criar uma nova conta? (s/n): ").lower()
        if criar == "s":
            conta = ContaCorrente(numero=str(len(contas) + 1), cliente=cliente)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print("Conta criada com sucesso!")

    def acessar_conta():
        cpf = input_cpf()
        cliente = encontrar_cliente_por_cpf(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return
        if not cliente.contas:
            print("Este cliente não possui contas.")
            return

        print("Contas disponíveis:")
        for idx, conta in enumerate(cliente.contas):
            print(f"[{idx}] Conta {conta.numero} - Agência {conta.agencia}")

        try:
            escolha = int(input("Escolha uma conta: "))
            conta = cliente.contas[escolha]
        except (ValueError, IndexError):
            print("Escolha inválida.")
            return

        while True:
            print("""
            === Menu Conta ===
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Voltar para escolha de contas
            [0] Voltar ao menu inicial
            """)
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Valor para depósito: R$ "))
                conta.depositar(valor)
            elif opcao == "2":
                valor = float(input("Valor para saque: R$ "))
                conta.sacar(valor)
            elif opcao == "3":
                conta.extrato()
            elif opcao == "4":
                return acessar_conta()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    while True:
        print("""
        ========== Menu Inicial ========== 
        [1] Criar novo cliente
        [2] Criar nova conta
        [3] Acessar conta
        [0] Sair
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            acessar_conta()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

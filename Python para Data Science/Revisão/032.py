'''
Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de cada aluno em um dicionário e todos os dicionários em uma lista.
No final mostre:
Quantas pessoas foram cadastradas
A média de idade do grupo
Uma lista com todas as mulheres
Uma lista com todas as pessoas com idade acima da média
'''

def cadastrar_aluno():
    """Função para cadastrar um aluno com validações"""
    aluno = {}

    aluno['nome'] = input("Nome do aluno: ").strip().title()

    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            aluno['sexo'] = sexo
            break
        else:
            print("Erro: Por favor, digite apenas 'M' ou 'F'.")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                raise ValueError("Idade não pode ser negativa.")
            aluno['idade'] = idade
            break
        except ValueError as e:
            print(f"Erro: {e}")

    return aluno


def mostrar_resultados(lista_alunos):
    """Função para mostrar os resultados finais"""
    total = len(lista_alunos)
    print(f"\nTotal de alunos cadastrados: {total}")

    media_idade = sum(aluno['idade'] for aluno in lista_alunos) / total
    print(f"Média de idade do grupo: {media_idade:.2f} anos")

    mulheres = [aluno['nome'] for aluno in lista_alunos if aluno['sexo'] == 'F']
    print(f"Lista de mulheres: {', '.join(mulheres) if mulheres else 'Nenhuma'}")

    acima_da_media = [aluno for aluno in lista_alunos if aluno['idade'] > media_idade]
    print("Pessoas com idade acima da média:")
    for aluno in acima_da_media:
        print(f"  Nome: {aluno['nome']}, Sexo: {aluno['sexo']}, Idade: {aluno['idade']}")


def main():
    alunos = []

    while True:
        aluno = cadastrar_aluno()
        alunos.append(aluno)

        continuar = input("Deseja cadastrar outro aluno? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    if alunos:
        mostrar_resultados(alunos)
    else:
        print("Nenhum aluno foi cadastrado.")


if __name__ == "__main__":
    main()
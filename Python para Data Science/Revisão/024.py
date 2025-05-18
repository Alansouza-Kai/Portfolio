def numero_por_extenso():
    numeros_extenso = (
        "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
        "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze"
    )

    try:
        numero = int(input("Digite um número entre 0 e 15: "))
        if 0 <= numero <= 15:
            print(f"Você digitou o número: {numeros_extenso[numero]}")
        else:
            print("Erro: número fora do intervalo permitido (0 a 15).")
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número inteiro.")

# Executa a função
numero_por_extenso()
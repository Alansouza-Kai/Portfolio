#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000


while True:
    try:
        numero = input("Digite o número desejado: ")
        if numero == '0000':
            break
        else:
            for i in range(11):
                resultado = int(numero) * i
                print(f"{numero} x {i} = {resultado}")
    except:
        print("Apenas aceitamos numeros")

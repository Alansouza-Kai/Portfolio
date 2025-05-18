'''Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:
Quantas pessoas foram cadastradas
Uma listagem com as pessoas com o maior QI
Uma listagem com as pessoas de menor QI
'''
#loop para o usuário não quebrar o programa colocando letras no lugar de números
def loop():
    try:
        Lista[1].append(int(input("Desculpe, apenas aceitamos números inteiros no QI, tente novamente: ")))
    except:
        loop()

#Função para criar uma lista
def temp():
    Listatemp.append(Lista[0][:])
    Listatemp.append(Lista[1][:])

#listas usadas
Lista = [[],[]]
Listatemp = []
Maiorqi = []
Menorqi = []

#Para alimentar a lista
while True:
    Nome = input("Digite o nome da pessoas ou digite 'sair' para finalizar: ").strip().lower()
    if Nome == "sair":
        break
    else:
        Lista[0].append(Nome)
        try:
            Lista[1].append(int(input("Digite o valor do QI: ")))
        except:
            while len(Lista[1]) < len(Lista[0]):
                loop()

temp()

#ordena do maior para o menor usando uma lista temporária
while len(Listatemp[0]) > 0:
    maior = max(Listatemp[1])
    Posiçãomaior = (Listatemp)[1].index(maior)
    Maiorqi.append(Listatemp[0][Posiçãomaior])
    Listatemp[0].pop(Posiçãomaior)
    Listatemp[1].pop(Posiçãomaior)

Listatemp.clear()
temp()

#ordena do menor para o maior, usando uma lista temporária
while len(Listatemp[0]) > 0:
    menor = min(Listatemp[1])
    Posiçãomenor = (Listatemp)[1].index(menor)
    Menorqi.append(Listatemp[0][Posiçãomenor])
    Listatemp[0].pop(Posiçãomenor)
    Listatemp[1].pop(Posiçãomenor)

#impressão dos dados
print(f'No total foram cadastradas {len(Lista[0])} pessoas')
print(f'Os maiores Qis em ordem são as seguintes pessoas {Maiorqi}')
print(f'Os Menores Qis em ordem são as seguintes pessoas {Menorqi}')



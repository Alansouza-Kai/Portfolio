#Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas.
# Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].

Lista1 = [1,2,3,4,5]
Lista2 = [5,4,3,2,1]
Lista3 = []
Continuar = "s"

'''
while Continuar != "n":
    Lista1.append(int(input("Digite o valor para adicionar na lista 1: ")))
    Lista2.append(int(input("Digite o valor para adicionar na lista 2: ")))
    Continuar = input("Deseja continuar? [S/N]").strip().lower()[0]
'''

for i in range (0, len(Lista2)):
    V1 = Lista1[i]
    V2 = Lista2[i]
    Soma = V1 + V2
    Lista3.append(Soma)

print(Lista1)
print(Lista2)
print(Lista3)
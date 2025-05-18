#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

#Entrada de dados:

D1 = float(input("Digite sua nota: "))
D2 = float(input("Digite sua nota: "))
D3 = float(input("Digite sua nota: "))
D4 = float(input("Digite sua nota: "))
D5 = float(input("Digite sua nota: "))

#lógica
Média = (D1 + D2 + D3 + D4 + D5)/5

if  Média < 6:
    print("sua média é insuficiente")
elif    Média >= 6 and  Média<7:
    print("sua média é suficiente")
elif    Média >= 7 and  Média<9:
    print("sua média é Boa")
else:
    print("sua média é excelente")

'''
Correção:

if  Média >= 9:
    print("sua média é excelente")
elif    Média >7:
    print("Sua média é Boa")
elif    Média >6:
    print("Sua média é suficiente")
else:
    print("Sua média é insuficiente")
'''
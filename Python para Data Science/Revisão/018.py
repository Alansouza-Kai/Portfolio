'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre:

Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato
'''

Nomes = []
Preços = []
Continue = "S"
M1000 = 0
PBarato = None
Mvalor = None

while True:
    Nome = input("Nome do produto: ")
    Preço = float(input("Preço do produto: ").replace(",","."))
    Nomes.append(Nome)
    Preços.append(Preço)
    Continue = input("Deseja continuar? [S/N]").strip().lower()[0]
    if Preço > 1000.00:
        M1000 += 1
    if Mvalor == None:
        PBarato = Nome
        Mvalor = Preço
    if Mvalor > Preço:
        PBarato = Nome
        Mvalor = Preço
    if Continue == "n":
        break

print(f'O Total gasto na compra foi {sum(Preços)} Reais')
print(f'{M1000} produtos no carrinho, custam mais que R$1000,00')
print(f'O produto de menor valor é o {PBarato}')



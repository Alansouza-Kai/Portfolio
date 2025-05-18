#Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input("Digite sua palavra aqui: ").strip().lower()

#resolução

pontos = 0

for i in range (0, len(palavra)):
    if  palavra[i] == palavra[-i-1]:
        pontos = pontos+1
if pontos == len(palavra):
    print('É um palindromo')
else: print('Não é')

#só para pular linha
print(" ")

#correção

if  palavra == palavra[::-1]:
    print('É um palindromo')
else:
    print('Não é')
'''Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

Frase = input('Escreva sua frase: ').strip().lower().replace('á','a').replace('à','a').replace('ã','a').replace('â','a').replace('ä','a')

print(Frase.count('a'))
print(Frase.find('a'))
print(Frase.rfind('a'))

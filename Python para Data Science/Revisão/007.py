#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

Letra = input('Digite uma letra: ').lower().strip()[0]
if Letra in 'aeiouáà':
    print(f'A letra "{Letra}" é uma vogal')
else:
    print(f'A letra "{Letra}" é uma consoante')


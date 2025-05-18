#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

#entrada de dados
Letra = input('Digite uma letra: ').lower().strip()[0]

#lógica

if Letra in 'aeiouáàãâäéèêëíìîïóòõôöúùûü':
    print(f'A palavra começa com a vogal "{Letra}"')
elif    Letra in "0123456789":
    print('É para escrever uma palavra, não um número. Tente novamente!!')
else:
    print(f'A palavra começa com a consoante "{Letra}"')

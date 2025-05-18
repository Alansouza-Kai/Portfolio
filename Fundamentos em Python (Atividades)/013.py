'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

#Entrada de dados
Frase = input("Digite a sua frase: ").strip()

#processamento de dados extra feito com compreensão inicial

d1 = Frase.count('a')
d2 = Frase.count('A')
d3 = Frase.count('á')
d4 = Frase.count('Á')
d5 = Frase.count('à')
d6 = Frase.count('À')
d7 = Frase.count('ã')
d8 = Frase.count('Ã')
d9 = Frase.count('â')
d10 = Frase.count('Â')
d11 = Frase.count('ä')
d12 = Frase.count('Ä')
Valortotal = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12

#Resolução pedida
Quantidade = Frase.count('a')
primeira = Frase.find("a")
Última = Frase.rfind("a")

#saída de dados
print(f'Na frase existem {Quantidade} letras "a"'
      f'\nA primeira letra "a" aparece na posição: {primeira}'
      f'\nA útima letra "a" aparece na posição: {Última}'
      f'\nO Valor total considerando diferentes grafias é: {Valortotal}')

#Correção

Frase1 = input("Digite a sua frase: ").strip().lower()

Frase1 = Frase1.replace('á','a')
Frase1 = Frase1.replace('à','a')
Frase1 = Frase1.replace('ã','a')
Frase1 = Frase1.replace('â','a')

print(f'primeiro a? {Frase1.find("a") + 1}'
      f'\nÚltimo a? {Frase1.rfind("a") + 1}'
      f'\nQuantos as? {Frase1.count("a")}')
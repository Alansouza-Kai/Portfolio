"""
Escreva um programa que leia o

Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
"""
#Minha resolução

Homemvelhon = "N/A"
HomemvelhoI = 0
Idades = 0
mulheres20 = 0

for i in range(1,5):
    nometemp = input("Estreva seu nome: ").strip().lower()
    idade = int(input("Escreva sua idade: "))
    sexotemp = input("Qual é o seu Sexo? ").strip().lower()[0]
    if  sexotemp == 'm':
        if idade > HomemvelhoI:
            HomemvelhoI = idade
            Homemvelhon = nometemp
            Idades = Idades + idade
        else:
            Idades = Idades + idade
    elif sexotemp == 'f':
        if idade < 20:
            mulheres20 = mulheres20 + 1
            Idades = Idades + idade
        else:
            Idades = Idades + idade
    else:
        Idades = Idades + idade

print(f'A média de idade do grupo é: {Idades/4}\nO homem mais velho do grupo é o: {Homemvelhon}\nExistem {mulheres20} mulheres com menos de 20 anos no grupo')

#espaçamento
print("")

#Correção

soma_idades = 0
idade_h_m_velho = 0
nome_h_velho = ""
quantidadem = 0

for j in range(4):
    nome = input("Estreva seu nome: ").strip().lower()
    idade2 = int(input("Escreva sua idade: "))
    sexo = input("Qual é o seu Sexo? ").strip().upper()[0]

    #
    soma_idades += idade2

    #2
    if  sexo == 'M' and idade2 > idade_h_m_velho:
        idade_h_m_velho = idade2
        nome_h_velho = nome

    #3
    if sexo == "F" and  idade2 <20:
        quantidadem +=1

print(f'A média de idade do grupo é: {soma_idades/4}\n'
      f'O homem mais velho do grupo é o: {nome_h_velho}\n'
      f'Existem {quantidadem} mulheres com menos de 20 anos no grupo')

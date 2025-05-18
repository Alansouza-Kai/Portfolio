#Operações Mataméticas
'''print(12 + 123)
print(89858 - 9)
print(56 * 9989)
print(57 / 24)
print(23 ** 54 ) #simbolo para exponenciação

#print com texto
print('Olá Mundo')

#print formatado (texto + Virgula)
idade = 29
print(idade)
print(f'Sua idade é {idade}')#O f na fente das aspas, serve para buscar dados além de apenas escrever.

#leitura de dados
nome = input('Digite seu nome: ')
idade= input('Digite sua idade: ')
print(f'Seu nome é {nome}, e sua idade é {idade} anos')

#tipos de Dados

idade_1 = int(input('Digite a primeira idade: ')) #int para converter em numeros inteiros, float para numeros flutuantes
idade_2 = int(input('Digite a segunda idade: '))
soma_idades = idade_1 + idade_2  #Soma de textos é concatenar.
print(f'A soma das idades é {soma_idades}')


# Strings

Senai = 'Luis Eulálio'
#Fatiamento
print(Senai[0])
print(Senai[3:7])
print(Senai[:5])
print(Senai[7:])

#Análise

print(len(Senai))#quantas letras tem ao todo
print(Senai.count('l')) #frequencia de termos
print(Senai.find("E")) #onde está?

#manipulação do dado
#Senai = Senai.upper() Sobreposição de dados
print(Senai.upper()) #converter para maiusculoo
print(Senai.lower()) #tudo em minúsculo
print(Senai.replace('L','P')) #substituir
print(Senai)


nome = input('Nome: ').strip() #remover espaços antes e depois
Print(nome)


#Condicionais

altura = float(input('Altura: '))

#1
if altura > 1.2:
    print('pode andar no brinquedo')
else:
    print('Quem sabe ano que vem!')
#2
if altura > 2:
    print('Você vai bater a cabeça')
elif altura < 1.2:
    print('Quem sabe ano que vem!')
else:
    print('Ta liberado!!!')

#criação de jogos aleatórios
import ramdom

PC = random.randit( )
print(pc)



#for

for i in range(1,10): #o ultimo valor não conta, apenas considera a difereça até chegar nele, nesse caso, 9
    print(*)

for i in range(1,10):
    print(i)

for i in range(10,1,-1):#o terceiro é o "range" de contagem, sendo nnegativo, de tras para frente
    print(i)

soma = 0
for i in range(1, 10):
    n = int(input("Valor: "))
    soma = soma + n
    print(soma)


#while

contador = 0
while contador < 5:
    print('OI')
    contador += 1

#parada com string
resposta = ''

while resposta != "N"
    print("bem vindo")
    resposta = input('deseja continuar [S/N]').strip().upper()[0]

'''
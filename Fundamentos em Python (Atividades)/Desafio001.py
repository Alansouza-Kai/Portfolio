#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

#Entrada de dados
posicaoinicial = float(input("Digite o valor da posição inicial: "))
velocidadeinicial = float(input("Digite o valor da velocidade inicial: "))
aceleracao = float(input("Digite o valor da aceleração: "))
tempo = float(input("Digite o valor de tempo: "))

#Formula do MRUV
'''
S=Si+Vi*t+((a*t**2)/2)
'''
Posicao = posicaoinicial + (velocidadeinicial * tempo) + ((aceleracao * tempo **2)/2)

#Saída de dados:
print(f"A posição do objeto no tempo {tempo} é de {Posicao}(m)")



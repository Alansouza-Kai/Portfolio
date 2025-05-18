#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time
#definição de variáveis

PC = random.randint(1,3)
user = int(input(f'Vamos jogar Jokenpo!\n1: Pedra\n2: papel\n3: Tesoura\nDigite o número equivalente aqui: '))

#método 1
print("Método 1")

if  PC == 1 and user == 1:
    print("A máquina escolheu Pedra.\nVocês empataram")
elif    PC == 1 and user == 2:
    print("A máquina escolheu Pedra.\nParabens, você ganhou.*__*")
elif    PC == 1 and user == 3:
    print("A máquina escolheu Pedra.\nQue pena, você perdeu.;-;")
elif    PC == 2 and user == 1:
    print("A máquina escolheu Papel\nQue pena, você perdeu.;-;")
elif    PC == 2 and user == 2:
    print("A máquina escolheu Papel\nVocês empataram.")
elif    PC == 2 and user == 3:
    print("A máquina escolheu Papel\nParabens, você ganhou.*__*")
elif    PC == 3 and user == 1:
    print("A máquina escolheu Tesoura\nParabens, você ganhou.*__*.")
elif    PC == 3 and user == 2:
    print("A máquina escolheu Tesoura\nQue pena, você perdeu.;-;")
elif    PC == 3 and user == 3:
    print("A máquina escolheu Tesoura\nVocês empataram.;-;")
else:
    print("Você digitou um número fora dos programados")

#só para dar espaçamento

print("")

#método 2
print("Método 2")

if  (PC == 1 and user == 1) or (PC == 2 and user == 2) or (PC == 3 and user == 3):
    print(f"A máquina escolheu {PC}.\nVocês empataram")
elif    (PC == 1 and user == 2) or (PC == 2 and user == 3) or (PC == 3 and user == 1):
    print(f"A máquina escolheu {PC}.\nParabens, você ganhou.*__*")
elif    (PC == 1 and user == 3) or (PC == 2 and user == 1) or (PC == 3 and user == 2):
    print(f"A máquina escolheu {PC}.\nQue pena, você perdeu.;-;")
else:
    print("Você digitou um número fora dos programados")

#só para dar espaçamento

print("")

'''
#correção
print("Correção")

#time serve para colocar o "delay" e tempo entre uma ação e outra.
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
print('Ainda Pensando...')
time.sleep(1)

if  PC == user:
    print(f"A máquina escolheu {PC}.\nVocês empataram")
elif    (PC == 1 and user == 2) or (PC == 2 and user == 3) or (PC == 3 and user == 1):
    print(f"A máquina escolheu {PC}.\nParabens, você ganhou.*__*")
else:
    print(f"A máquina escolheu {PC}.\nQue pena, você perdeu.;-;")
'''
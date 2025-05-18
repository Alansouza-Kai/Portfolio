#Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas: matemática, português e história.
# Em seguida, exiba a média das notas dos alunos.

def loop1():
    try:
        NotaMatematica.append(int(input("Desculpe, apenas aceitamos números para as notas, tente novamente: ")))
    except:
        loop1()

def loop2():
    try:
        NotaPortuguês.append(int(input("Desculpe, apenas aceitamos números para as notas, tente novamente: ")))
    except:
        loop2()

def loop3():
    try:
        NotaHistória.append(int(input("Desculpe, apenas aceitamos números para as notas, tente novamente: ")))
    except:
        loop3()


Contador = 0
NotaMatematica = []
NotaPortuguês = []
NotaHistória = []
Notas = {}

while True:
    Nome = input("Digite o nome do aluno ou digite 'sair' para finalizar: ").strip().lower()
    if Nome == "sair":
        break
    else:
        try:
            NotaMatematica.append(int(input("Digite a nota de Matemática: ")))
        except:
            loop1()
        try:
            NotaPortuguês.append(int(input("Digite a nota de Português: ")))
        except:
            loop2()
        try:
            NotaHistória.append(int(input("Digite a nota de História: ")))
        except:
            loop3()
        Contador += 1
        for i in range(Contador):
            Notas[Nome] = {
                "Matematica": NotaMatematica[i],
                "Português": NotaPortuguês[i],
                "História": NotaHistória[i]
            }

print(Notas)
print(f'A média das notas em Matemática é {(sum(NotaMatematica)/Contador)}'
      f'\nA média das notas em Português é {(sum(NotaPortuguês)/Contador)}'
      f'\nA média das notas em História é {(sum(NotaHistória)/Contador)}')

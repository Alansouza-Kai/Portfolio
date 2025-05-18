#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Coleta de dados
N1 = int(input('Digite um número: '))

#Calculo dobro
dobro = N1 * 2

#Calculo triplo
triplo = N1 * 3

#Calculo raiz quadrada
raiz = N1 ** (1/2)

#Saída de dados

print(f'O dobro de {N1} é : {dobro} \nO triplo de {N1} é : {triplo} \nA raiz de {N1} é : {raiz:.2f}')

'''
#Correção print

print(f'O dobro de {N1} é : {dobro} \n'
      f'O triplo de {N1} é : {triplo} \n'
      f'A raiz de {N1} é : {raiz}')

print(f'O dobro de {N1} é : {N1 * 2} \n'
      f'O triplo de {N1} é : {N1 * 3} \n'
      f'A raiz de {N1} é : {N1 ** (0.5)}')
'''
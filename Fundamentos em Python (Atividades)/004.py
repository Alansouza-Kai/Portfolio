#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#Coleta de dados
raio = float(input('Digite o raio da esfera: '))

#Calculo volume da esfera
Volume = (4/3)*3.1415*(raio**3)

#Calculo area da esfera
area = 4*3.1415*(raio**2)

#Saída das informações
print(f'Volume da Esfera: {Volume}')
print(f'Área da esfera: {area}')

'''
Correção do Professor

#Coleta de dados
raio = float(input('Digite o raio da esfera: '))
#Calculo volume da esfera
Volume = (4/3)*3.1415*raio**3
#Calculo area da esfera
area = 4*3.1415*raio**2
#Saída das informações
print(f'Volume da Esfera: {Volume:.2f}\nÁrea da esfera: {area:.2f}')
'''
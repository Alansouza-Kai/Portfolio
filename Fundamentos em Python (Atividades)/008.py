#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

#entrada de dados
Salario = float(input('Digite o valor do seu salário: '))

#calculo
poncentagem = Salario * 0.60
valorfinal = Salario + poncentagem

#Saída de dados
print(f"O salário de {Salario} com o reajuste de 60% será de: {valorfinal}")

'''correção

print(f"O salário de {Salario} com o reajuste de 60% será de: {Salario * 1.6}")
'''

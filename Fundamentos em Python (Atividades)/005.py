#Escreva um programa que converta real para o Franco Congolês

#coleta de dados:
real = float(input('Digite o valor em reais: '))
franco = 499.75

#Conversão do valor
cambio = real * franco

#Saída de dados
print(f'{real} reais, equivalem a {cambio} Francos Congoleses')

#correçao metodo 2
#Saída de dados
print(f'{real} reais, equivalem a {real*franco} Francos Congoleses')



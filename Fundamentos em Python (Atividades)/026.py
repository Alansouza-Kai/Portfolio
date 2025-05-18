#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.


Peso = float(input('Digite o seu peso: ').replace(',','.'))
altura = float(input('Digite a sua altura em metros: ').replace(',','.'))


#Lógica
IMC = Peso * altura ** 2

if  IMC >= 30:
    print("Você está com obesidade")
elif    IMC > 25:
    print("Você está com sobrepeso")
elif    IMC > 18.5:
    print("Você está na média de peso ideal")
else:
    print("Você está abaixo do peso")
''''
1.Escreva um programa que leia, nome, idade, sexo e país de orígem.
2. Organize cada leitura como uma lista, e insira em outra lista de armazenamento.
3. Após isso, crie um data frame usando pandas com suas respectivas colunas.
4. Calcule usando pandas.
	4.1 média de idade
	4.2 moda de idade
	4.3 mediana da idade
'''

def Quebradelinha():
    print('-*-*-'*10)


import pandas as pd

Nome = ['Alan', "souza", 'Bezerra', 'Joana','Gertrudes']
Idade = [30,31,22,15,79]
Sexo = ['Masculino','Masculino','Sim, quero','Feminino','Feminino']
Pais = ['Brasil', "Portugal", "Italia", "Brasil", "Roma"]


Lista = {'Nome': Nome,'Idade': Idade,'Sexo': Sexo,'Pais': Pais}

df = pd.DataFrame(Lista)

Quebradelinha()
print(df)
Quebradelinha()
print(df['Idade'].mean())
Quebradelinha()
print(df['Idade'].mode())
Quebradelinha()
print(df['Idade'].median())
Quebradelinha()
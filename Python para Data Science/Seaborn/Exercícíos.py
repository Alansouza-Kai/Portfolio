
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd



def Quebradelinha():
    print(f"\033[38;5;165m{'-*-*-'*15}\033[0m")

#Importação de dados
titanic = pd.read_csv('Titanic-Dataset.csv')
print(titanic.columns)

sns.set_style('whitegrid')

#Exercicio 24
sns.jointplot(x='Fare',y ='Age',data=titanic)
plt.show()

#Exercício 25

sns.histplot(titanic['Fare'],bins=30, color='red')#plotagem de grafico histograma
plt.show()

#Exercício 26
sns.boxplot(x = 'Pclass',y = 'Age',data=titanic,palette='muted',hue='Pclass',legend=False)
plt.show()

#Exercício 27

sns.swarmplot(x='Pclass',y = 'Age',data=titanic,palette='flare',hue='Pclass',legend=False)
plt.show()

#Exercício 28

sns.countplot(x = 'Sex',data=titanic,hue = 'Sex')
plt.show()


#Exercício 29

g = sns.FacetGrid(data=titanic, col='Sex')
g.map(plt.hist,'Age')
plt.show()



#bibliotecas

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#setar paleta de cores
#sns.set_style('viridis')

gorgeta = sns.load_dataset('tips') #importação

#plotagem univariada (histograma)

sns.histplot(gorgeta['total_bill'],kde=True,bins=30)#plotagem de grafico histograma
plt.show()

#plotagem comparada
sns.jointplot(x='total_bill',y ='tip',data=gorgeta)
plt.show()

sns.jointplot(x='total_bill',y ='tip',data=gorgeta,kind='hex')
plt.show()

sns.jointplot(x='total_bill',y ='tip',data=gorgeta,kind='reg')
plt.show()

#criação de grafico para todas as variáveis numericas

sns.pairplot(gorgeta)
plt.show()

#criação de grafico para todas as variáveis numericas com filtro
sns.pairplot(gorgeta,hue='sex')
plt.show()

#rugplot
sns.rugplot(gorgeta['total_bill'])
plt.show()

#kde
sns.kdeplot(gorgeta['total_bill'])
plt.show()

#Plotagem de categorias

sns.barplot(x = 'sex',y = 'total_bill',data=gorgeta,estimator=np.sum)
plt.show()

sns.countplot(x = 'sex',data=gorgeta)
plt.show()

#DIagrama de caixas (boxplot)
sns.boxplot(x = 'day',y = 'total_bill',data=gorgeta,hue='smoker')
plt.show()


#Diagrama de Violino

sns.violinplot(x = 'day',y = 'total_bill',data=gorgeta,hue='sex',split=True)

#Stripplot
sns.stripplot(x='day',y = 'total_bill',data=gorgeta,jitter = True,hue = 'sex')
plt.show()

#swarmplot

sns.swarmplot(x='day',y = 'total_bill',data=gorgeta)
plt.show()


#Gráfico coringa

sns.catplot(x='day',y = 'total_bill',data=gorgeta, kind='bar')
plt.show()

#Plotagem de Matriz

voos = sns.load_dataset('flights')

#Mapa de calor

vp = voos.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(vp,cmap='viridis')
plt.show()

#mapa Cluster
sns.clustermap(vp,standard_scale=1)
plt.show()

#Grids

g = sns.FacetGrid(data=gorgeta, col='time',row='smoker')
g.map(sns.histplot,'total_bill')
plt.show()




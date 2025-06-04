import numpy as np
import pandas as pd

from numpy.random import randn

def Quebradelinha():
    print('-*-*-'*10)

'''
#Série de dados
#método 1 com listas

etiquetas = ['a','b','c']
dados = [10,20,30]

#método 2 com dicionários
arr = np.array(dados)
d = {"a": 10, "b": 20, "c": 30}

#usando o pandas para trasnformar em séries
#método 1 com lista
print(pd.Series(data=dados))
print(pd.Series(data=dados, index=etiquetas))
Quebradelinha()

#método 2 com dicionário
print(pd.Series(data=d))
Quebradelinha()

#Contrução de séries
ser1 = pd.Series([1,2,3,4],['EUA','Alemanha',"Italia","Japão"])
ser2 = pd.Series([4,3,2,1],['EUA','Alemanha',"Italia","Japão"])

#operações com séries
ser3 = ser1 + ser2
print(ser3)
ser3 = ser3*2
print(ser3)
print(ser1  >ser2)
Quebradelinha()

#acesso a elementos únicos
a = ser1["EUA"]
print(a)
Quebradelinha()

#Criação do Data Frame
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
print(df)
Quebradelinha()


#Acesso ao conteúdo do DF

print(df['w'])
print(df[['w','x']])
Quebradelinha()

#Criação de novas colunas
df['Nova'] = df['w'] + df ['z']
print(df["Nova"])
Quebradelinha()

#Remover Colunas
df.drop('w', axis=1, inplace= True)#axis é para representar que é uma coluna sendo apagada.#Já o Inplace, é para que a alteração seja efetivada no dataframe
df.drop('e', inplace=True) #sem o axis, o sistema entende que é para apagar a linha.

print(df)
Quebradelinha()

#Acesso de linhas
Linha_A = df.loc['a'] #acessa a linha pelo nome dela
Linha_A2 = df.iloc[0] #acessa a linha pelo valor da indexação

print(Linha_A)
print(Linha_A2)
Quebradelinha()

#Acesso a valores únicos
Idade = df.loc['b','x']
print(Idade)

Quebradelinha()

#Acesso a partes do DF
Parte1 = df.loc[['a','b'],['x','y']]
print(Parte1)
Quebradelinha()


#Seleção condicionada
Selec_Cond = df[df > 0 ]

Selec_Cond1 = df['w'] > 0
Selec_Cond2 = df[df['w'] > 0]
print(Selec_Cond1)
print(Selec_Cond2)

Coluna_Z_Positiva = df[df['z']>0]
Coluna_x_coluna_z_positiva = df[df['z']>0]['x']

Coluna_w_positiva_e_Coluna_y_positiva = df[(df['w']>0) & (df['y']>0)] #& faz a função and, e | faz a função OR.
print(Coluna_w_positiva_e_Coluna_y_positiva)


#Dados Faltantes

d = {'A':[1,2,np.nan],'B': [5,np.nan,np.nan], 'C': [1,2,3]} #np.nan serve para gerar dado nulo (vazio) na celula

df =pd.DataFrame(d)

print(df)
Quebradelinha()
print(df.isnull())#Conta quantos nulos (vazios)
Quebradelinha()
print(df.isnull().sum())#Retorna quantos nulos tem
Quebradelinha()
#remove todos os dados com linhas faltantes
print(df.dropna())
Quebradelinha()
#remove todos os dados com colunas faltantes
print(df.dropna(axis=1))
Quebradelinha()
#Remove todas as linhas que não tiverem pelo menos um na (nulo)
print(df.dropna(thresh=1)) #apaga turo que não tiver pelo menos o valor registrado (abaixo do valor)
Quebradelinha()
print(df.fillna(value=0)) #Troca os valores nulos pelo 0 (ou o que colocar no parenteses)
Quebradelinha()
'''

#Criação do Data Frame
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
print(df)
Quebradelinha()

#Estatistica
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df['w'].mean())
print(df['w'].median())
print(df['w'].mode())
print(df['w'].std()) #desvio padrão
print(df['w'].var()) #variancia
print(df['w'].sum())
print(df['w'].max())
print(df['w'].min())
print(df['w'].quantile(0.25))
print(df['w'].quantile(0.75))
print(df['w'].value_counts()) #contagem de valores
print(df['w'].unique()) #Valores não unicos
print(df['w'].nunique()) #VAlores únicos
print(df.corr()) #correlação
print(df.cov()) #covariancia
print(df.sort_values('w', ascending=False)) #Reorganiza a "tabela" (False maior para o menor, true, menor para o maior)
'''
def vezes2(X):
    return X*2

print(df['w'])
print(df['w'].apply(vezes2))
print(df['w'].apply(lambda X: X*2))


#Importação de dados
df = pd.read_excel('Nome exato do arquivo') #Excel
df = pd.read_csv('Nome exato do CSV')
df = pd.read_html('https://www.fdic.gov/bank-failures/failed-bank-list')

print(df.columns) #print colunas

print(df.head()) #print 5 primeiras
print(df.tail()) #print 5 ultimas
print(df.info()) #print informações da planilha
print(df.describe()) #print descrição completa da planilha
print(df)

#exportação de dados

df['Novo'] = df['quantidade']*10
df.to_excel('Planilha revisada.xlx',index=False)


#agrupar por

df = pd.read_excel('Base Aula 002 - Exemplo .xlsx')

print(df[['Vendedor','Peso','Quantidade','Total']].groupby('Vendedor').sum()) #está por vendedor, somando os valores de peso, quantidade e total
'''

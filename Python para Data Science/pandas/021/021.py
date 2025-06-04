'''1.Importe a Base Aula 002 - Exemplo.xlsx
2. Encontre a Informação
	2.1 - Qual país vendeu mais(Total)?
	2.2 - Qual o melhor vendedor?
	2.3 - Qual o melhor tipo de loja?
	2.4 - Qual é o tipo de envio mais usado?
	2.5 - Qual o público que mais atendemos (Gênero)?
	2.6 - Quem fez as 3 maiores vendas?
	2.7 - Adicione uma nova coluna comissão (Total * 5%)
'''
def Quebradelinha():
    print(f"\033[38;5;165m{'-*-*-'*15}\033[0m")


import pandas as pd

df = pd.read_excel('Base Aula 002 - Exemplo .xlsx')
#df['Total'] = (df['Quantidade'] * df['Preco']) * (1 - df['Desconto']) #atualização do total, pois os valores não batem

#Quebradelinha()
#print(df.head())
#Quebradelinha()

#print(df.columns)#para identificar as colunas
#Quebradelinha()

'''BLOCO 1 - Identificação do Pais com maior vendas'''
print("\033[38;5;213mQual país vendeu mais(Total)?\033[0m")

PaisMaior = df[['País','Quantidade','Total']].groupby('País').sum()
print(PaisMaior.sort_values('Quantidade', ascending=False).head(1))
Quebradelinha()

'''Bloco 2 - Identificação do melhor vendedor (Como não foi definido o critério de melhor, foi utilizado como base a média de vendas por vendedor x a média geral das vendas, para identificar os  vendedores que vendem acima da média'''

print("\033[38;5;213mQual o melhor vendedor?\033[0m")

#Para calcular a média de vendas por vendedor
media_por_vendedor = df.groupby('Vendedor')['Total'].mean().reset_index()
media_por_vendedor = media_por_vendedor.rename(columns={'Total': 'Média_Vendas'})
#print(media_por_vendedor)
#Quebradelinha()

#calcular a média geral de vendas
media_geral = df['Total'].mean()
#print(f"Média Geral de Vendas: {media_geral}")
#Quebradelinha()

#Compara cada vendedor com a média geral
media_por_vendedor['Relevância'] = media_por_vendedor['Média_Vendas'].apply(
    lambda x: 'Acima da Média' if x > media_geral else 'Abaixo da Média'
)

#Visualizar o Ranking dos melhores vendedores pela média de venda
ranking_vendedores = media_por_vendedor.sort_values(by='Média_Vendas', ascending=False)
print(ranking_vendedores.head(1))
Quebradelinha()

'''BLOCO 3 - Qual o melhor tipo de loja? (Foi usada a mesma lógica anterior, apenas mudando os valores'''
print("\033[38;5;213mQual o melhor tipo de loja?\033[0m")

#Para calcular a média de vendas por loja
media_por_loja = df.groupby('Loja')['Total'].mean().reset_index()
media_por_loja = media_por_loja.rename(columns={'Total': 'Média_Vendas'})
#print(media_por_loja)
#Quebradelinha()

#calcular a média geral de vendas
media_geral2 = df['Total'].mean()
#print(f"Média Geral de Vendas: {media_geral2}")
#Quebradelinha()

#Compara cada loja com a média geral
media_por_loja['Relevância'] = media_por_loja['Média_Vendas'].apply(
    lambda x: 'Acima da Média' if x > media_geral2 else 'Abaixo da Média'
)

#Visualizar o Ranking dos melhores Lojas pela média de venda
media_por_lojas = media_por_loja.sort_values(by='Média_Vendas', ascending=False)
print(media_por_lojas.head(1))
Quebradelinha()

'''BLOCO 4: Qual é o tipo de envio mais usado'''

print("\033[38;5;213mQual é o tipo de envio mais usado?\033[0m")

df_filtrado = df[df['Tipo de Envio'] != 'Loja Física'] #Filtro para remover "loja fisica", visto que isso não é um envio e sim retirada.
print(df_filtrado['Tipo de Envio'].value_counts().head(1)) #contagem de valores
Quebradelinha()

'''BLOCO 5:  Qual o público que mais atendemos (Gênero)?'''
print("\033[38;5;213mQual o público que mais atendemos (Gênero)?\033[0m")

print(df['Gênero'].value_counts().head(1)) #contagem de valores
Quebradelinha()

'''BLOCO 6: Quem fez as 3 maiores vendas?'''
print("\033[38;5;213mQuem fez as 3 maiores vendas?\033[0m")

maiores_3_vendas = df[['Vendedor','Total']].groupby('Vendedor').max()
print(maiores_3_vendas.sort_values('Vendedor', ascending=False).head(3))
Quebradelinha()

'''BLOCO 7 : Adicione uma nova coluna comissão (Total * 5%)'''

df['Comissão'] = df['Total'] * 0.05

'''BLOCO 8 : Exportando a planilha'''

df.to_excel('Planilha revisada.xlsx',index=False)



'''1. Importe a Vendas_Incorreto
2. Trate todos os dados incorretos
3. Analise estatisticamente o arquivo'''

def Quebradelinha():
    print(f"\033[38;5;165m{'-*-*-'*15}\033[0m")

import pandas as pd

#Importação da planilha (meu método)
#df = pd.read_excel('Vendas_Incorreto.xlsx')

#método professor
df2 = pd.read_excel('Vendas_Incorreto.xlsx')

#Ações usadas para identificar dados da planilha, como colunas vazias e numero de linhas preenchidas.
'''
Quebradelinha()
print(df.head())
Quebradelinha()
print(df.info())
print(df.columns)#para identificar as colunas
Quebradelinha()
'''

#TRATAMENTO DOS DADOS (meu método)

# Remover linhas vazias
#df = df.dropna(thresh=1)
# Remover colunas vazias
#df = df.dropna(thresh=1, axis=1)
#print(df.info())
#Quebradelinha()

#método professor

df = df2.dropna(how='all')
df = df.dropna(how='all',axis=1)

print(df.info())
print(df.isnull().sum())

# Preencher dados faltantes nas colunas críticas, se necessário
df['Ordem'] = df['Ordem'].ffill()
df['Loja'] = df['Loja'].fillna('Desconhecida')
df['Vendedor'] = df['Vendedor'].fillna('Desconhecido')
df['Produto'] = df['Produto'].fillna('Desconhecido')
df['Gênero'] = df['Gênero'].fillna('Não Informado')

# Corrigir tipos de dados
df['Ordem'] = df['Ordem'].astype(int)
df['Quantidade'] = df['Quantidade'].fillna(0).astype(int)
df['Preço de Compra'] = df['Preço de Compra'].fillna(0)

# Corrigir colunas de datas
for col in ['Data Pedido', 'Data Pagamento', 'Data Envio', 'Data Entrega']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

print(df.head())
Quebradelinha()

#Analise estatisticamente o arquivo

# Estatísticas gerais
print("\033[38;5;213mDados do Dataframe\033[0m")
print(df.describe(include='all'))
Quebradelinha()

# Total de vendas
total_vendas = df['Total'].sum()
print("\033[38;5;213mTotal de Vendas:\033[0m", total_vendas)
Quebradelinha()

# Média de vendas por pedido
media_vendas = df['Total'].mean()
print("\033[38;5;213mMédia de Vendas por Pedido:\033[0m", media_vendas)
Quebradelinha()

# Produtos mais vendidos
mais_vendidos = df['Produto'].value_counts()
print("\033[38;5;213mProdutos mais vendidos:\033[0m", mais_vendidos)
Quebradelinha()

# Vendas por loja
vendas_por_loja = df.groupby('Loja')['Total'].sum()
print("\033[38;5;213mVendas por loja:\033[0m", vendas_por_loja)
Quebradelinha()

# Quantidade de itens vendidos por vendedor
Quantidade_por_vendedor = df.groupby('Vendedor')['Quantidade'].sum()
print("\033[38;5;213mQuantidade produtos por vendedor:\033[0m", Quantidade_por_vendedor)
Quebradelinha()

# Devoluções
devolucoes = df['Devolucao'].value_counts()
print("\033[38;5;213mDevoluções:\033[0m", devolucoes)
Quebradelinha()

#Dos métodos e envio, qual é o mais utilizado considerando apenas a compra?

df_filtrado = df[df['Tipo de Envio'] != 'Loja Física'] #Filtro para remover "loja fisica", visto que isso não é um envio e sim retirada.
print(df_filtrado[f'Tipo de Envio'].value_counts()) #contagem de valores
Quebradelinha()

#Qual método de retirada, vende mais produtos por vez?

df_consolidado = df[['Tipo de Envio','Quantidade']].groupby('Tipo de Envio').agg('sum')
print(f'\033[38;5;213mQual método de retirada, vende mais produtos por vez?\033[0m{df_consolidado.sort_values('Quantidade',ascending=False)}')

#Exportação da planilha
df.to_excel('Planilha revisada.xlsx',index=False)

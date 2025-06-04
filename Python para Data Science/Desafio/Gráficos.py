import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import squarify
import numpy as np
import matplotlib.patheffects as path_effects

# Carregar o dataset
df = pd.read_csv('winemag-data-130k-v2.csv')
df.rename(columns={df.columns[0]: 'ID'}, inplace=True)

# Tratamento
df['country'].fillna('Desconhecido', inplace=True)
df['province'].fillna('Desconhecida', inplace=True)
df['region_1'].fillna('Desconhecida', inplace=True)
df['region_2'].fillna('Desconhecida', inplace=True)
df['taster_name'].fillna('Anônimo', inplace=True)
df['taster_twitter_handle'].fillna('Anônimo', inplace=True)

# Estilo dos gráficos
sns.set(style="whitegrid")

# ========================== 5.1 Panorama Geral ==========================

# Gráfico 1 - Barplot dos países

plt.figure(figsize=(10,6))
ax = sns.countplot(
    y='country',
    data=df,
    order=df['country'].value_counts().head(10).index,
    palette='magma'
)

plt.title('Top 10 Países com Mais Vinhos', color='#ffc0cb')

# Adicionar os rótulos nas barras
plt.figure(figsize=(10,6))
ax = sns.countplot(
    y='country',
    data=df,
    order=df['country'].value_counts().head(10).index,
    palette='magma'
)

plt.title('Top 10 Países com Mais Vinhos', color='#ffc0cb')

# Adicionar os rótulos nas barras
for p in ax.patches:
    width = p.get_width()
    plt.text(
        width + 5,
        p.get_y() + p.get_height()/2,
        int(width),
        ha='left', va='center',
        color='#ffc0cb',
        fontsize=10, fontweight='bold'
    )

# Remove os títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Colore os números das escalas dos eixos (opcional, se quiser seguir a estética)
ax.tick_params(colors='#ffc0cb')

# Fundo do plot (área dos dados)
plt.gca().set_facecolor('none')
# Fundo da figura inteira
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico1_paises.png', transparent=True)
plt.close()


# Gráfico 2 - Treemap dos países

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,6))
ax = plt.gca()

# Desenha o treemap normalmente
squarify.plot(
    sizes=top_countries.values,
    label=top_countries.index + '\n' + top_countries.values.astype(str),
    alpha=0.8,
    color=sns.color_palette('magma', len(top_countries)),
    text_kwargs={'color': '#ffc0cb', 'fontsize':10, 'weight':'bold'},
    ax=ax
)

# Aplica borda vinho nos textos gerados pelo squarify.plot
for txt in ax.texts:
    txt.set_path_effects([
        path_effects.Stroke(linewidth=2.5, foreground='#75155c'),  # borda vinho
        path_effects.Normal()
    ])

plt.title('Distribuição dos Vinhos por País', color='#75155c')

plt.axis('off')
plt.gca().set_facecolor('none')  # Fundo do plot (área dos dados)
plt.gcf().set_facecolor('none')  # Fundo da figura inteira

plt.tight_layout()
plt.savefig('grafico2_treemap.png', transparent=True)
plt.close()


# Gráfico 3 - Barplot das variedades

plt.figure(figsize=(10,6))
ax = sns.countplot(
    y='variety',
    data=df,
    order=df['variety'].value_counts().head(10).index,
    palette='magma'
)

plt.title('Top 10 Variedades de Vinho', color='#ffc0cb')

# Adicionar os rótulos nas barras
for p in ax.patches:
    width = p.get_width()
    plt.text(
        width + 5,
        p.get_y() + p.get_height()/2,
        int(width),
        ha='left', va='center',
        color='#ffc0cb',
        fontsize=10, fontweight='bold'
    )

# Remove os títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Colore os números das escalas dos eixos
ax.tick_params(colors='#ffc0cb')

# Fundo da área dos dados
plt.gca().set_facecolor('none')
# Fundo da figura inteira
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico3_variedades.png', transparent=True)
plt.close()


# Gráfico 4 - Vinícolas mais populares

top_wineries = df['winery'].value_counts().head(10)

plt.figure(figsize=(10,6))
ax = sns.barplot(
    x=top_wineries.values,
    y=top_wineries.index,
    palette='magma'
)

plt.title('Top 10 Vinícolas Mais Populares', color='#ffc0cb')

# Adicionar os rótulos numéricos nas barras
for p in ax.patches:
    width = p.get_width()
    plt.text(
        width + max(top_wineries.values)*0.01,  # Pequeno deslocamento proporcional
        p.get_y() + p.get_height()/2,
        int(width),
        ha='left', va='center',
        color='#ffc0cb',
        fontsize=10, fontweight='bold'
    )

# Remove os títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Colore os números das escalas dos eixos
ax.tick_params(colors='#ffc0cb')

# Fundo da área dos dados
plt.gca().set_facecolor('none')
# Fundo da figura inteira
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico4_vinicolas.png', transparent=True)
plt.close()



# Gráfico 5 - WordCloud das descrições
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Gerando a WordCloud com paleta magma
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Gerando a WordCloud com fundo transparente e paleta magma
text = ' '.join(df['description'].dropna())
wordcloud = WordCloud(
    width=1600,
    height=800,
    background_color=None,  # <-- Fundo transparente
    mode='RGBA',            # <-- Necessário para transparência
    colormap='magma'
).generate(text)
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Palavras Mais Frequentes nas Descrições')
plt.tight_layout()

# Salvar com fundo transparente
plt.savefig('grafico5_wordcloud.png', transparent=True)
plt.close()



# ========================== 5.2 Qualidade ==========================

# Gráfico 6 - Boxplot pontos por país

# Filtra os top 10 países mais frequentes
top_countries = df['country'].value_counts().head(10).index

# Calcula as medianas para esses países
median_points = df[df['country'].isin(top_countries)].groupby('country')['points'].median()

# Ordena os países pela mediana em ordem decrescente
top_countries_sorted = median_points.sort_values(ascending=False).index

plt.figure(figsize=(10,6))
ax = sns.boxplot(
    x='points',
    y='country',
    data=df[df['country'].isin(top_countries_sorted)],
    order=top_countries_sorted,   # Aqui aplicamos a ordem
    color='#823347'
)

# Título na cor rosa pastel
ax.set_title('Distribuição de Pontos por País', color='#75155c')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Números das escalas (ticks) na cor rosa pastel
ax.tick_params(axis='x', colors='#75155c')
ax.tick_params(axis='y', colors='#75155c')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Rótulos numéricos nas caixas: medianas dos pontos para cada país
for i, country in enumerate(top_countries_sorted):
    median = median_points[country]
    # y_pos: posição da categoria no eixo y, invertida pelo seaborn automaticamente
    y_pos = i
    ax.text(median, y_pos, f'{median:.1f}', color='#ffc0cb', va='center', ha='left', fontsize=9)

plt.tight_layout()

# Salvar com fundo transparente
plt.savefig('grafico6_pontos_pais.png', transparent=True)
plt.close()



# Gráfico 7 - Violinplot pontos por região

top_regions = df['region_1'].value_counts().head(10).index
median_points = df[df['region_1'].isin(top_regions)].groupby('region_1')['points'].median()
top_regions_sorted = median_points.sort_values(ascending=False).index

plt.figure(figsize=(10,6))
ax = sns.violinplot(
    x='points',
    y='region_1',
    data=df[df['region_1'].isin(top_regions_sorted)],
    order=top_regions_sorted,
    color='#823347'
)

ax.set_title('Distribuição de Pontos por Região', color='#ffc0cb')
ax.set_xlabel('')
ax.set_ylabel('')
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico7_pontos_regiao.png', transparent=True)
plt.close()



# Gráfico 8 - Histograma das pontuações

plt.figure(figsize=(10,6))
ax = sns.histplot(
    df['points'],
    kde=True,
    bins=20,
    color='#823347'
)

# Título na cor padrão (sem path effect)
ax.set_title('Distribuição das Pontuações', color='#75155c')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks simples na cor rosa (sem borda)
ax.tick_params(axis='x', colors='#75155c')
ax.tick_params(axis='y', colors='#75155c')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Rótulos numéricos nas barras do histograma (com path effects)
for patch in ax.patches:
    height = patch.get_height()
    if height > 0:
        txt = ax.text(
            patch.get_x() + patch.get_width() / 2,
            height,
            f'{int(height)}',
            ha='center',
            va='bottom',
            color='#ffc0cb',
            fontsize=9,
            weight='bold'
        )
        txt.set_path_effects([
            path_effects.Stroke(linewidth=2.5, foreground='#75155c'),  # borda vinho
            path_effects.Normal()
        ])

plt.tight_layout()

# Salvar com fundo transparente
plt.savefig('grafico8_hist_pontos.png', transparent=True)
plt.close()

# Gráfico 9 - Tendência de pontos ao longo dos anos (se tiver coluna 'vintage' ou 'year')
# Supondo que o ano esteja na coluna 'title' (extração simples):

df['year'] = df['title'].str.extract(r'(\d{4})').astype(float)

# Filtrar apenas os anos entre 1903 e 2050
df = df[(df['year'] >= 1903) & (df['year'] <= 2050)]

# Calcular a média dos pontos por ano
year_points = df.groupby('year')['points'].mean().dropna()

# Criar o gráfico
plt.figure(figsize=(10, 6))
ax = sns.lineplot(
    x=year_points.index,
    y=year_points.values,
    color='#823347'
)

# Título na cor rosa pastel
ax.set_title('Média de Pontos por Ano', color='#ffc0cb')

# Labels dos eixos
ax.set_xlabel('Ano', color='#ffc0cb')
ax.set_ylabel('Pontuação Média', color='#ffc0cb')

# Cor dos ticks dos eixos
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Salvar o gráfico
plt.tight_layout()
plt.savefig('grafico9_pontos_ano.png', transparent=True)
plt.close()



# Gráfico 10 - Boxplot pontuação por degustador
plt.figure(figsize=(10,6))
top_tasters = df['taster_name'].value_counts().head(10).index

# Calcula a mediana dos pontos por degustador para ordenar
median_points = df[df['taster_name'].isin(top_tasters)].groupby('taster_name')['points'].median()
top_tasters_sorted = median_points.sort_values(ascending=False).index

ax = sns.boxplot(
    x='points',
    y='taster_name',
    data=df[df['taster_name'].isin(top_tasters_sorted)],
    order=top_tasters_sorted,
    color='#823347'
)

# Título na cor rosa pastel
ax.set_title('Pontuação por Degustador', color='#75155c')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#75155c')
ax.tick_params(axis='y', colors='#75155c')

# Fundo transparente
ax.patch.set_alpha(0)
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Rótulos numéricos medianos em rosa pastel, do lado das caixas
for i, taster in enumerate(top_tasters_sorted):
    median = median_points[taster]
    y_pos = i
    ax.text(median, y_pos, f'{median:.1f}', color='#ffc0cb', va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.savefig('grafico10_taster.png', transparent=True)
plt.close()



# ========================== 5.3 Preço e Economia ==========================

# Gráfico 11 - Boxplot preço por país

median_price = df[df['country'].isin(top_countries)].groupby('country')['price'].median()
top_countries_sorted = median_price.sort_values(ascending=False).index

plt.figure(figsize=(10,6))
ax = sns.boxplot(
    x='price',
    y='country',
    data=df[df['country'].isin(top_countries_sorted)],
    order=top_countries_sorted,
    color='#823347',
    showfliers=False  # Remove outliers visuais
)

plt.xscale('log')  # Escala logarítmica

# Título na cor rosa pastel
ax.set_title('Preço dos Vinhos por País', color='#75155c')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#75155c')
ax.tick_params(axis='y', colors='#75155c')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Rótulos numéricos medianos em rosa pastel do lado das caixas (x = mediana)
for i, country in enumerate(top_countries_sorted):
    median = median_price[country]
    y_pos = i
    ax.text(median, y_pos, f'{median:.2f}', color='#ffc0cb', va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.savefig('grafico11_preco_pais.png', transparent=True)
plt.close()


# Gráfico 12 - Histograma dos preços

# Filtra preços até 500 dólares
price_filtered = df['price'].dropna()
price_filtered = price_filtered[price_filtered <= 500]

plt.figure(figsize=(10,6))
ax = sns.histplot(
    price_filtered,
    bins=40,
    kde=True,
    color='#823347'
)

# Título na cor rosa pastel
ax.set_title('Distribuição dos Preços dos Vinhos (até 500$)', color='#ffc0cb')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks em rosa pastel
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Rótulos numéricos nas barras
for patch in ax.patches:
    height = patch.get_height()
    if height > 0:
        ax.text(
            patch.get_x() + patch.get_width() / 2,
            height,
            f'{int(height)}',
            ha='center',
            va='bottom',
            color='#ffc0cb',
            fontsize=9
        )

plt.tight_layout()
plt.savefig('grafico12_preco_500.png', transparent=True)
plt.close()


# Gráfico 13 - Scatter preço vs pontos
plt.figure(figsize=(10,6))
ax = sns.scatterplot(
    x='price',
    y='points',
    data=df,
    color='#823347'
)

plt.xscale('log')

# Título na cor rosa pastel
ax.set_title('Preço vs Pontuação', color='#ffc0cb')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico13_preco_pontos.png', transparent=True)
plt.close()


# Gráfico 14 - Evolução do preço no tempo
# Carregar a base de dados
df = pd.read_csv("winemag-data-130k-v2.csv")

# Extrair o ano da coluna 'title' e converter para float
df['year'] = df['title'].str.extract(r'(\d{4})').astype(float)

# Filtrar apenas os anos entre 1903 e 2050
df = df[(df['year'] >= 1903) & (df['year'] <= 2050)]

# Calcular a média de preço por ano
year_price = df.groupby('year')['price'].mean().dropna()

# Criar o gráfico
plt.figure(figsize=(10, 6))
ax = sns.lineplot(
    x=year_price.index,
    y=year_price.values,
    color='#823347'
)

# Título na cor rosa pastel
ax.set_title('Média de Preço por Ano', color='#ffc0cb')

# Remover os rótulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Salvar o gráfico
plt.tight_layout()
plt.savefig('grafico14_preco_ano.png', transparent=True)
plt.close()


#Tabela :
top10_expensive = df.dropna(subset=['price']).sort_values(by='price', ascending=False).head(10)
plt.figure(figsize=(12, 4))
plt.axis('off')
plt.title('', fontsize=16, fontweight='bold')
tabela = plt.table(
    cellText=top10_expensive[['title', 'price', 'points']].values,
    colLabels=['Nome do Vinho', 'Preço (USD)', 'Pontuação'],
    cellLoc='center',
    loc='center'
)
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1, 2)
plt.gcf().set_facecolor('none')
for key, cell in tabela.get_celld().items():
    cell.set_facecolor('none')
    cell.set_edgecolor('#823347')
plt.tight_layout()
plt.savefig('./tabela_top10_vinhos_caros.png', transparent=True)
plt.close()




# ========================== 5.4 Custo-benefício ==========================

# Gráfico 15 - Scatter preço vs pontos com popularidade
df['value_for_money'] = df['points'] / df['price']

plt.figure(figsize=(10,6))
ax = sns.scatterplot(
    data=df,
    x='price',
    y='points',
    size='value_for_money',
    sizes=(20, 200),
    color='#823347',
    alpha=0.5
)

plt.xscale('log')

# Título na cor rosa pastel
ax.set_title('Custo-benefício: Preço vs Pontuação', color='#ffc0cb')

# Remove títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico15_custo_beneficio.png', transparent=True)
plt.close()

# Gráfico 16 - Top 10 vinhos custo-benefício

top_value = df.sort_values(by='value_for_money', ascending=False).head(10)

plt.figure(figsize=(10,6))
ax = sns.barplot(
    x=top_value['value_for_money'],
    y=top_value['title'],
    palette='magma'
)

# Título na cor rosa pastel
ax.set_title('Top 10 Vinhos Custo-Benefício', color='#ffc0cb')

# Remover títulos dos eixos
ax.set_xlabel('')
ax.set_ylabel('')

# Ticks na cor rosa pastel
ax.tick_params(axis='x', colors='#ffc0cb')
ax.tick_params(axis='y', colors='#ffc0cb')

# Fundo transparente
ax.set_facecolor('none')
plt.gcf().set_facecolor('none')

# Ajustar limite direito para dar espaço aos números
x_max = top_value['value_for_money'].max()
plt.xlim(0, x_max * 1.1)  # 10% a mais na margem direita

# Espaço extra para afastar o texto 3 pixels (aprox 3% do eixo x)
offset = x_max * 0.03

# Rótulos numéricos fora da barra, alinhados à esquerda e afastados
for p in ax.patches:
    width = p.get_width()
    y = p.get_y() + p.get_height() / 2
    ax.text(
        width + offset,
        y,
        f'{width:.2f}',
        va='center',
        ha='left',
        color='#ffc0cb',
        fontsize=9
    )

plt.tight_layout()
plt.savefig('grafico16_top_custo_beneficio.png', transparent=True)
plt.close()


# ========================== 5.5 Variedades ==========================

# Gráfico 17 - Boxplot pontos por variedade
top_varieties = df['variety'].value_counts().head(10).index

# Ordenação dos dados pela mediana dos pontos (do maior para o menor)
order = df[df['variety'].isin(top_varieties)].groupby('variety')['points'].median().sort_values(ascending=False).index

# Gráfico
plt.figure(figsize=(10,6))
sns.boxplot(
    x='points',
    y='variety',
    data=df[df['variety'].isin(top_varieties)],
    color='#823347',
    order=order
)

# Título e estética
plt.title('Pontuação por Variedade', color='#ffc0cb')
plt.xlabel('')
plt.ylabel('')
plt.xticks(color='#ffc0cb')
plt.yticks(color='#ffc0cb')

# Fundo transparente
plt.gca().set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico17_variedade.png', transparent=True)
plt.close()

# ========================== 5.6 Degustadores e Descrição ==========================

# Gráfico 18 - WordCloud de vinhos com mais de 95 pontos
text_high = ' '.join(df[df['points'] >= 95]['description'].dropna())

# Gera a WordCloud com fundo transparente
wordcloud_high = WordCloud(
    width=1600,
    height=800,
    background_color=None,
    mode='RGBA',
    colormap='magma'
).generate(text_high)

# Plot
plt.figure(figsize=(12,6))
plt.imshow(wordcloud_high, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud - Vinhos com Pontuação ≥ 95', color='#ffc0cb')

# Fundo transparente
plt.gca().set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico18_wordcloud_95.png', transparent=True)
plt.close()

# Gráfico 19 - Scatter comprimento descrição vs pontos
df['desc_length'] = df['description'].apply(lambda x: len(str(x)))

# Plot
plt.figure(figsize=(10,6))
sns.scatterplot(
    x='desc_length',
    y='points',
    data=df,
    alpha=0.3,
    color='#823347'
)

plt.title('Comprimento da Descrição vs Pontuação', color='#ffc0cb')

# Remove labels dos eixos
plt.xlabel('')
plt.ylabel('')

# Cor das escalas
plt.xticks(color='#ffc0cb')
plt.yticks(color='#ffc0cb')

# Fundo transparente
plt.gca().set_facecolor('none')
plt.gcf().set_facecolor('none')

plt.tight_layout()
plt.savefig('grafico19_desc_pontos.png', transparent=True)
plt.close()

# ========================== 5.7 Tendências Temporais ==========================

# Gráfico 20 - Heatmap ano vs preço e pontos
# Cria a tabela dinâmica
pivot = df.pivot_table(index='year', values=['points', 'price'], aggfunc='mean')

# Plot
plt.figure(figsize=(10,6))

# Linha para Pontuação
sns.lineplot(
    x=pivot.index,
    y=pivot['points'],
    label='Pontuação Média',
    color='#823347'
)

# Linha para Preço
sns.lineplot(
    x=pivot.index,
    y=pivot['price'],
    label='Preço Médio',
    color='#ffc0cb'
)

# Título
plt.title('Pontuação e Preço ao Longo dos Anos', color='#ffc0cb')

# Remove os labels dos eixos
plt.xlabel('')
plt.ylabel('')

# Cor dos números das escalas
plt.xticks(color='#ffc0cb')
plt.yticks(color='#ffc0cb')

# Fundo transparente
plt.gca().set_facecolor('none')
plt.gcf().set_facecolor('none')

# Legenda com padrão
plt.legend(facecolor='none', edgecolor='none', labelcolor='#ffc0cb')

plt.tight_layout()
plt.savefig('grafico20_linhas.png', transparent=True)
plt.close()



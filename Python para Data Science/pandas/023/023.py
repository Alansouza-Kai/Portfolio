'''
Crie um programa que
Importe a biblioteca pandas como pd
Leia um DataFrame “Salarios.csv” e nomei-o de df
Retorne o head do DataFrame
Use o método .info(), para descobrir quantas entradas ele tem
Qual é a média de Pagamento Base?
Qual é o maior montante pago em OvertimePay?
Qual é a profissão do ‘JOSEPH DRISCOLL’
Qual o nome da pessoa mais bem paga
Qual é a media de pagamento base por ano?
Quantas profissoes únicas existem?

'''
def Quebradelinha():
    print(f"\033[38;5;165m{'-*-*-'*15}\033[0m")

import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('Salaries.csv')

# 1. Mostrar as primeiras linhas do DataFrame
print("\033[38;5;213mRetorne o head do DataFrame\033[0m")
print(df.head())
Quebradelinha()

# 2. Informações gerais sobre o DataFrame
print("\033[38;5;213mInformações do DataFrame\033[0m")
print(df.info())
Quebradelinha()

# 3. Média do Pagamento Base
media_pagamento_base = df['BasePay'].mean()
print(f"Média de Pagamento Base: {media_pagamento_base:.2f}")
Quebradelinha()

# 4. Maior montante pago em OvertimePay
maior_overtime = df['OvertimePay'].max()
print(f"Maior valor em OvertimePay: {maior_overtime:.2f}")
Quebradelinha()

# 5. Profissão de 'JOSEPH DRISCOLL'
profissao_joseph = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values
if len(profissao_joseph) > 0:
    print(f"Profissão de JOSEPH DRISCOLL: {profissao_joseph[0]}")
else:
    print("JOSEPH DRISCOLL não encontrado no DataFrame.")
Quebradelinha()

# 6. Pessoa mais bem paga (TotalPayBenefits)
pessoa_mais_bem_paga = df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName'].values
if len(pessoa_mais_bem_paga) > 0:
    print(f"Pessoa mais bem paga: {pessoa_mais_bem_paga[0]}")
else:
    print("Não foi possível encontrar a pessoa mais bem paga.")
Quebradelinha()

# 7. Média de pagamento base por ano
media_pagamento_ano = df.groupby('Year')['BasePay'].mean()
print("=== Média de Pagamento Base por Ano ===")
print(media_pagamento_ano)
Quebradelinha()

# 8. Número de profissões únicas
num_profissoes_unicas = df['JobTitle'].nunique()
print(f"Número de profissões únicas: {num_profissoes_unicas}")
Quebradelinha()

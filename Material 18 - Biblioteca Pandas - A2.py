# Biblioteca pandas
# Leitura, conversão e salvamento de dados de um DataFrame

import pandas as pd
import os
os.system('cls')

# Leitura e conversão CSV
df = pd.read_csv(r'./output/Material 10 - Vendas (Bruto).csv', delimiter=';')
print('DataFrame completo:\n', df.head(), '\n')

# Últimos registros
print('DataFrame completo:\n', df.tail(10), '\n')

# Informações sobre as colunas
print('DataFrame completo:\n', df.info(), '\n')

# Tipos de dados
print('DataFrame completo:\n', df.dtypes, '\n')

# Trocar o índice
novo_indice = df['CPF']
df.index = novo_indice
print(df.head())

# Exportar os dados de um DataFrame
# Excel (Pasta de Trabalho)

df.to_excel(r'./output/Material 18 - Vendas Bruto.xlsx', index=False)
print('\nArquivo gerado com sucesso!\n')

# pyarrow
df.to_parquet(r'./output/Material 18 - Vendas Bruto.parquet', engine='pyarrow', index=False)
print('\nArquivo gerado com sucesso!\n')

# JSON
df.to_json(r'./output/Material 18 - Vendas Bruto.json', orient='records', lines=True)
print('\nArquivo gerado com sucesso!\n')


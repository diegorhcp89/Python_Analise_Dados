# análise de dados com pandas
import pandas as pd
from os import system

system('cls')

# Leitura do arquivo
dados_csv = pd.read_csv(filepath_or_buffer='Material 26 - Vendas.csv', sep=';', encoding='utf-8')
#print(dados_csv.head())

# Verificar se há dados nulos
print('Existencia de dados nulos:\n', dados_csv.isna().sum())
print()

# Aplicar um filtro para valores nulos
print('Dados nulos encontrados:\n', dados_csv[dados_csv.isna().any(axis=1)],'\n')

# Substituir dados nulos por "NÃO IDENTIFICADO" na coluna CIDADE

dados_csv['CIDADE'] = dados_csv['CIDADE'].fillna('NÃO IDENTIFICADO')
dados_csv['DATA E HORA COMPRA'] = dados_csv['DATA E HORA COMPRA'].fillna('01/01/1900 00:00')
print('Correção dos valores nulos:\n', dados_csv, '\n')

# Aplicar um filtro para valores nulos
print('Dados nulos encontrados:\n', dados_csv[dados_csv.isna().any(axis=1)], '\n')

dados_csv['MES'] = dados_csv['DATA E HORA COMPRA'].str[3:5]
dados_csv['MES'] = pd.to_numeric(dados_csv['MES'])
print(dados_csv.head())

# Coluna refêrencia
dados_csv['REFERENCIA'] = dados_csv['DATA E HORA COMPRA'].str[6:10] + \
                          dados_csv['DATA E HORA COMPRA'].str[3:5]
print(dados_csv.head())

# Exportar o Dataframe
dados_csv.to_csv(r'.\output\Material 27 - Vendas - análise.csv',
                 sep=';',
                 encoding='utf-8',
                 index=False)

print('Processo parcialmente concluido...')
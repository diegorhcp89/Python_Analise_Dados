# Biblioteca Pandas
# Conversão de Valores

import pandas as pd
import os

os.system('cls')

# Forma 1: to_numeric()
lista_valores = pd.Series(['1.0', '2', '-3', '5', '7', '9'])

soma_valores_inicial = lista_valores.sum()
print('Somatória:', soma_valores_inicial, '\n')

# Converter para o formato numérico
valores_convertidos_m1 = pd.to_numeric(lista_valores)
soma_valores = valores_convertidos_m1.sum()
print('Valores convertidos:', soma_valores, '\n')

# Forma 2: astype()

valores_convertidos_m2 = lista_valores.astype('float')
soma_valores = valores_convertidos_m2.sum()
print('Valores convertidos:', soma_valores, '\n')

# Exemplo 2
df_1 = pd.read_csv(r'.\output\Material 10 - Vendas (Bruto).csv', delimiter=';')
soma_valores = df_1['VALOR_NOTA'].sum()
print('Total recebido:', soma_valores, '\n')

# Função anônima - Função lambda
df_1['VALOR_NOTA'] = pd.to_numeric(df_1['VALOR_NOTA'].apply(lambda x: x.replace(',', '.')).astype('float'))
soma_valores = df_1['VALOR_NOTA'].sum()
print('Total recebido:', round(soma_valores), '\n')

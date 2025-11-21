# Biblioteca Pandas
# DataFrames e Series

import pandas as pd
print('\033c')

# Criação de um dataframe (dictionary)
lista_pessoas = {
    "NOME": ['Alessandro', 'Marcia', 'Simone', 'Joao'],
    "IDADE": [53, 49, 17, 21],
    "SEXO": ['M', 'F', 'F', 'M']
}

df = pd.DataFrame(lista_pessoas) # Tabela biodimensional (linhas e colunas)
print(df)

# Series é uma coluna do DataFrame
print('Series Nomes:\n', df['NOME'], '\n', sep='')

# Criação de Series
valores = [450, 888, 17, 99]
valores_series = pd.Series(valores, index=['VLA_A', 'VL_B', 'VL_C', 'VL_D'])
print('Valores:\n', valores_series, '\n')
print('Tipo:', type(valores_series), '\n')

# Acessar elementos de uma Serie
print('Primeiro valor:', valores_series[0])

# Adicionar uma nova coluna ao DataFrame
mes_aniversario = pd.Series([11, 7, 3, 12])
df['MES_ANIV'] = mes_aniversario

print(df.head())

# Métodos de Series no DataFrame
print('\nMaior idade:', df['IDADE'].max())
print('\nMenor idade:', df['IDADE'].min())
print('\nQtd Nomes:', df['IDADE'].count())

# Estatistica completa
print(df.describe())

print('Tipos de dados:\n', df.dtypes, '\n', sep='')

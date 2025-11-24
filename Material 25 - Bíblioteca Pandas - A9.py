# Bíbliotaca Pandas - Aula 9
# Método iloc

import pandas as pd
import os

os.system('cls')

# Utiliza índices inteiros para acessar os dados.
# Acessa linhas e colunas pela posição (indice numérico)
# Inclui o ponto inicial, mas exclui o ponto final ao selecionar intervalos.

df = pd.read_excel('Material 24 - Vendas.xlsx')
# print(df.head())

# Primeira linha
print('Primeiro registro:\n', df.iloc[0])

# Várias linhas
print('Varias linhas:\n', df.iloc[:50])

# Dez últimas linhas
print('Últimas linha:\n', df.iloc[-10])

# Selecionar a segunda coluna da primeira linha
print('NOME:', df.iloc[0, 1], '\n')

# Selecionar as 10 primeiras linhas e a segunda coluna
print('Resultado:', df.iloc[:10, 1:2], '\n')

print('\033c')

# Modificar o nome
df.iloc[0, 1] = 'Luana Lima Souza'
print(df.head())

print(df.loc[df['NOME'] == 'Luana Lima Souza'])

# Selecionar um intervalo de linhas e todas as colunas
intervalo = df.iloc[1:3, :]
print(intervalo)

# Biblioteca Pandas - Aula 9
# Métodos loc

import pandas as pd
import os

os.system('cls')

# Método loc
df = pd.read_excel('Material 24 - Vendas.xlsx', sheet_name='VENDAS')

# Método loc: Utiliza rótulos (labels) para acessar os dados
# Pode ser usado para acessar linhas e colunas por seus nomes.
# Inclui tanto o pondo inicial quando o ponto final ao selecionar intervalos.

# Retornar linhas específicas
print('Primeiro registro:\n', df.loc[0]) # Base 0
print('Três primeiros registros:\n,', df.loc[0:2])
print('A partir do vigésimo registro:\n', df.loc[20:])
print()

# Acessar registro especifico
nome = 'Juan Araújo'
print('Registro cliente:\n', df.loc[df['NOME'] == nome])
print()

# Vendas acima de 950
vendas_acima_950 = df.loc[df['VALOR_NOTA'] > 950]
print('Quantidade de vendas:', vendas_acima_950[0])
print()

# Pesquisa entre valores
entre_valores = df.loc[(df['VALOR_NOTA'] >= 500) & (df['VALOR_NOTA'] < 600)]
print(entre_valores)
print()

nome_filtrado = df.loc[df['NOME'].str.contains('Silva', regex=False)]
print(nome_filtrado)
print()

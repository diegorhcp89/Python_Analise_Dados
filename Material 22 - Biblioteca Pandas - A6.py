# Biblioteca Pandas
# Gravação no prório arquivo Excel

import pandas as pd
import os

os.system('cls')

nome_arquivo = 'Material 22 - Notas.xlsx'
df = pd.read_excel(nome_arquivo)

print(df.head())
exit()

colunas_notas = ['Nota_1', 'Nota_2', 'Nota_3', 'Nota_4']
df[colunas_notas] = df[colunas_notas].apply(pd.to_numeric)

df['Media'] = df[colunas_notas].mean(axis=1)
print('Calculo da média:\n', df, sep='')

with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode=a, if_sheet_exists='overlay') as writer:
    df.to_excel(writer, index=False, sheet_name='MÉDIAS_CALCULADAS')

print('Notas atualizadas...')
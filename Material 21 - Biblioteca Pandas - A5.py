# Biblioteca Pandas
# Ler dados a partir do Excel e manipulá-los

import pandas as pd
import os

os.system('cls')

df = pd.read_excel('Material 21 - Notas.xlsx')
# print(df.head)

colunas_notas = ['Nota_1', 'Nota_2', 'Nota_3', 'Nota_4']
df[colunas_notas] = df[colunas_notas].apply(pd.to_numeric)

df['Media'] = df[colunas_notas].mean(axis=1)
print('Calculo da média:\n', df, sep='')

df.to_excel(r'.\output\Material 21 - Médias calculadas.xlsx', index=False)

print('Notas atualizadas...')
# Bíblioteca Pandas - Aula 7
# Resultado em nova coluna (Aprovado e Reprovado)

import pandas as pd
import shutil
import os

os.system('cls')

nome_arquivo = r'.\output\Material 23 - Notas - Status.xlsx'

if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)

shutil.copy('Material 23 - Notas.xlsx', nome_arquivo)

df = pd.read_excel(nome_arquivo)

#print(df.head())

colunas_notas = ['Nota_1', 'Nota_2', 'Nota_3', 'Nota_4']
df[colunas_notas] = df[colunas_notas].apply(pd.to_numeric)

df['Media'] = df[colunas_notas].mean(axis=1)
print('Calculo da média:\n', df, sep='')

# Criar a situação do aluno
df['Aprovado'] = df['Media'].apply(lambda x: 'Sim' if x > 5 else 'Não')
print('Status do aluno:\n', df)

excel = pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='replace')
df.to_excel(excel, index=False, sheet_name='RESULTADOS')
excel.close()

print('Notas atualizadas...')
# Bíblioteca Pandas
# Leitura de Dados de um DataFrame e filtro de dados

import pandas as pd
import os
os.system('cls')

df = pd.read_csv(r'./output/Material 10 - Vendas (Bruto).csv', delimiter=';')

# Ler os dados
print('NOME:\n', df['NOME'].head(), '\n')

# Ler várias colunas
print('Várias colunas:\n', df[['NOME', 'CIDADE', 'IDADE']])
print('Nomes únicos:', df['NOME'].nunique(), '\n')

# Aplicar filtros
acima_80_anos = df[df['IDADE'] > 80]
print(acima_80_anos.head())
print('Qtd.Pessoas acima 80 anos:', acima_80_anos.shape[0], '\n')

# Selecionar 2 cidades
lista_cidades = ['Casa Grande', 'Cirino']
duas_cidades_m1 = df[df['CIDADE'].isin(lista_cidades)]
print('Cidades filtradas:\n', duas_cidades_m1)
print('Qtd.registros:', duas_cidades_m1.shape[0])

duas_cidades_m2 = df[(df['CIDADE'] == 'Casa Grande') |
                     (df['CIDADE'] == 'Cirino')]
print('Cidades filtradas:\n', duas_cidades_m2)
print('Qtd Registros:', duas_cidades_m2.shape[0])



# Biblioteca numpy

import numpy as np
import os
os.system('cls')

# Gear lista
lista_1 = np.array(range(1, 11))
print(lista_1, '\n')

# Remodelar matriz
lista_2 = lista_1.reshape(5, 2)
print(lista_2, '\n')

# Aplicação de filtros
print(lista_2[lista_2 < 4])
print(lista_2[lista_2 >= 7])
print('Números pares:', lista_2[lista_2 % 2 == 0])
print('Números impares:', lista_2[lista_2 % 2 == 1])
print(lista_2[(lista_2 >= 2) & (lista_2 <= 7)])

# Operações com matrizes
print('Somatória', lista_2.sum())
print('Maior valor:', lista_2.max())
print('Menor valor:', lista_2.min())
print('Média', lista_2.mean())
print('Valores únicos:', np.unique(lista_2))
print('Transpor:', lista_2.T)

# Calculo de média de vendas diárias

vendas_diarias = np.array(np.random.randint(2000, 4000, size=15))
#print(vendas_diarias)

for i in range(len(vendas_diarias)):
    print(f'Venda {i+1}: R$ {vendas_diarias[i]:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.'))

media_vendas = np.mean(vendas_diarias)
print(f'Média de venda diária:R$ {media_vendas:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.'))

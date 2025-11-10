# Biblioteca random
# Aula 2

import random as rd
import os

os.system('cls')

# Controlar a sequência de números aleatorios
print('1º Nr.:', rd.random(), '\n') # Estado atual do gerador

estado_gerado = rd.getstate() # Capture o estado atual interno do gerador
print('2º Nr.:', rd.random(), '\n')

rd.setstate(estado_gerado)
print('3º Nr.:', rd.random(), '\n')

# Função random.seed(a=None)
rd.seed(1234)
print('Valores aleatoris com seed 1234:')
valores_aleatorios = [rd.random() for n in range(30)]
print('Valores aleatorios:', valores_aleatorios, '\n')

# Simulação de vendas diárias para análise no BI
dias = 30
vendas_diarias = [rd.randint(80, 200) for n in range(dias)]
print('Vendas simuladas nos últimos 30 dias:\n', vendas_diarias, '\n')

media_vendas = sum(vendas_diarias) / dias
print(f'Média de vendas diárias: {media_vendas:.2f}', '\n')

# Simulação de previsão de vendas para ps próximos 7 dias
previsao_vendas = [int(media_vendas + rd.uniform(-20, 20)) for n in range(7)]
print('Previsão de vendas para os próximos 7 dias:', previsao_vendas, '\n')

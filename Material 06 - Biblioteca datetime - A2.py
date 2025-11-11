# Cálculo de churn de clientes
# Esse cálculo é importante para empresas que desejam entender
# a taxa de perda de clientes ao longo do tempo.

import datetime as dt
from datetime import datetime, timedelta
import os

os.system('cls')

cadastros = [
    datetime(2023, 1, 15),
    datetime(2023, 3, 22),
    datetime(2023, 5, 10),
    datetime(2023, 7, 5),
    datetime(2023, 8, 30)
]

cancelamentos = [
    datetime(2023, 6, 15),
    datetime(2023, 9, 1),
    None, # Cliente ativo
    datetime(2023, 8, 10),
    None # Cliente ativo
]

agora = datetime.now()

# Calcular tempo de permanência de cada cliente
# zip: iterador que combina elementos de 2 listas, formando

print('Tempo de permanência dos clientes (em dias):')

for cadastro, cancelamento in zip(cadastros, cancelamentos):
    if cancelamento:
        tempo = (cancelamento - cadastro).days
        print(f'Cliente cadastrado em {cadastro.strftime("%d/%m/%Y")} : {tempo} dias')
    else:
        tempo = (agora - cadastro).days
        print(f'Cliente cadastrado em {cadastro.strftime("%d/%m/%Y")} : {tempo} dias (ativo)')
print()

# Calcular taxa de churn (cancelamento)
total_clientes = len(cadastros)
clientes_cancelados = sum(1 for c in cancelamentos if c is not None)
taxa_churn =  clientes_cancelados / total_clientes * 100

print(f'\nTaxa de churn: {taxa_churn:.2f}%', '\n')
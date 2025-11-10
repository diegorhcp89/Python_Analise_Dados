# Biblioteca math
# Diferentes formas de importação

# Forma 1
# import math

# Forma 2
# import math as m # alias

# Forma 3
# from math import *

# Forma 4
# from math import pi

import math as m
import os

os.system('cls')

valor_pi = m.pi
print(valor_pi, '\n')

print('Número absoluto:', m.fabs(-5.66))
print('PI:', m.pi)
print('Truncar:', m.trunc(valor_pi))
print('Arredondar para cima:', m.ceil(3.3788))
print('Arredondar para baixo:', m.floor(3.3788))
print('Combinações', m.comb(25, 3))
print('Raiz quadrada:', round(m.sqrt(1888), 2))
print('Raiz cúbica:', m.cbrt(300))
print('Potência:', m.pow(2, 9))
print('NaN', m.nan) # Not a number
print('IsNan:', m.isnan(m.nan))

retorno = m.nan
print('Verificar se é NaN:', m.isnan(retorno), '\n')

retorno = m.isnan(m.nan)

if retorno:
    print('Verificar se é NaN: Sim!', '\n')
else:
    print('Verificar se é NaN: Não', '\n')

print()

# Exemplo prático: Cálculo de crescimento percentual de vendas usando logarismo
# Suponha que as vendas de uma empresa cresceram de 100 mil para 150 mil em 2 anos.

# Taxa de crescimento anual composta (CAGR)
# CAGR pode ser utilizada para medir o crescimento de vendas,
# receita ou qualquer outra métrica ao longo do tempo.

venda_inicial = 100000
venda_final = 150000
periodo = 2 # anos

cagr = (m.pow(venda_final / venda_inicial, 1 / periodo) - 1) * 100

print(f'Crescimento percentual anual composta (CAGR): {cagr:.2f}%\n')
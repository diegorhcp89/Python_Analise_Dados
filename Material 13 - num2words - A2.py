# Biblioteca num2words
# Exemplo prático

from num2words import num2words as nw
from os import system as sys
sys('cls')

qtd = 50
valor_faturamento = 1589111.32

print('RELATORIO FINANCEIRO'.center(qtd, '-'))
print(f'Faturamento total R$ {valor_faturamento:,.2f}'.replace(',','x').replace('.',',').replace('x', '.'))
print('\nFaturamento por extenso:')
print(nw(valor_faturamento, lang='pt_BR', to='currency').capitalize())

print()
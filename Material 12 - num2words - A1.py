# Biblioteca num2words
# Converte números em palavras

from num2words import num2words as nw
from os import system as sys

sys('cls')

qtd = 50

# Extenso dos números em inglês
print(nw(qtd))
print(nw(qtd + 0.77))
print(nw(18, 'ordinal'))

# Extenso em português
print(nw(qtd, lang='pt_br'))
print(nw(1234.89, lang='pt_br'))

# Valores Monetarios
print('VALORES MONETÁRIOS'.center(qtd, '-'))
print(nw(1300.87, lang='pt_BR'))
print(nw(1300, lang='pt_BR'), 'reais')

print(nw(1300, lang='pt_BR'), 'reais e', nw(87, lang='pt_BR'), 'centavos')
print(nw(1300.87, lang='pt_BR', to='currency'))

print(nw(125.32, lang='pt_BR', to='currency'), '\n')

print('VALORES MONETÁRIOS ESTRANGEIROS'.center(qtd, '-'))
print(nw(qtd, lang='es_ES', to='currency'))
print(nw(qtd, lang='ko'))
print(nw(qtd, lang='ja'))
print(nw(qtd, lang='ru'))

print('ANO'.center(qtd, '-'))
print('Ano de', nw(2025, lang='pt_BR', to='year'))


print()
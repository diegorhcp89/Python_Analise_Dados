# Biblioteca random
# Números randônicos

import random as rd
import os

os.system('cls')

# Números inteiros
print('randRange: ', rd.randrange(1, 60), '\n') 

# Geração de valores aleatorios em listas
lista_valores = rd.sample(range(61), 6)
print('Lista (original):', lista_valores, '\n')

# Classificação de listas
# Sorted
print('Classificada (sorted):', sorted(lista_valores), '\n')

# Sort (altera a lista original)
lista_valores.sort()
print('Classificada (sort):', lista_valores, '\n')

# Números inteiros aleatorios
print('randint:', rd.randint(1, 90), '\n')

# Seleção aleatoria de elementos
print('Seleção aleatória 1:', rd.choice(lista_valores), '\n')
print('Seleção aleatoria 2:',
      rd.choice(['Item A', 'Item B', 'Item C', 'Item D']), '\n')

# Embaralhamento
print('Lista original (classificada):', lista_valores)
rd.shuffle(lista_valores)
print('Lista embaralhada:', lista_valores, '\n')

# Lotofácil
print('Lotofácil:', sorted(rd.sample(range(1, 26), 15)), '\n')
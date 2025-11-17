# Biblioteca numpy
#
# Matriz Unidimensional [1][2][3][4]
# Matriz Bidimensional  [1][2][3]
#                       [4][5][6]
#                       [7][8][9]

import numpy as np
import os
os.system('cls')

# Criar um array como uma lista
array_1 = np.array([1, 2, 3, 4])
print(array_1)
print(type(array_1), '\n')
print(array_1[0], '\n')

# Substituição de um valor
array_1[0] = 100
print(array_1, '\n')
array_1[[1, 2, 3]] = 101, 102, 103
print(array_1, '\n')

# Array Multidimensional
array_2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(array_2, '\n')

# Atributos
print('Dimensões:', array_2.ndim, '\n')
print('Número de elementos:', array_2.shape)
print('Tamanho:', array_2.size, '\n')
print('Tipo de dados', array_2.dtype, '\n')

# Criação de arrays básicos
print('Array com zeros:', np.zeros(9))
print('Array com o número 1:', np.ones(8))
print('Elementos sequenciais:', np.arange(6))
print('Elementos espaçados:', np.arange(150, 200, 5))
print('Elementos espaçados linearmente:', np.linspace(0, 30, num=9))
print()
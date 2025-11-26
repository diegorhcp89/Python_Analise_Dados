# Bíblioteca matplotlib
# Dataviz no Python

import matplotlib.pyplot as plt
from pylab import plot, show, legend, title, xlabel, ylabel, axis
import os

os.system('cls')

# Gráfico simples
plt.plot(['A', 'B', 'C', 'D'], [1, 7, 4, 8])
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.title('Primeiro gráfico matplotlib')
plt.show()

# Gráfico com marcadores
eixo_x = ['A', 'B', 'C', 'D']
eixo_y = [1, 7, 4, 8]

plot(eixo_x, eixo_y, marker='x')
show()

# Gráfico com múltiplas séries
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul',
         'Ago', 'Set', 'Out', 'Nov', 'Dez']
Tmax = [38, 39, 32, 29, 26, 22, 19, 15, 20, 22, 25, 27]
Tmin = [23, 23, 22, 21, 19, 16, 12, 10, 16, 21, 22, 22]

plot(meses, Tmax, meses, Tmin)
title('Temperatura Máximo e Mínimo no ano')
xlabel('Mês')
ylabel('Temp/°C')
legend(['TMax', 'TMin'])
axis(ymin=0, ymax=41)
show()

# Gráfico de Pizza

rotulos = 'Python', 'C++', 'Ruby', 'Java'
sizes = [40, 30, 20, 11]
cores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=rotulos, colors=cores,
        autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')

plt.show()
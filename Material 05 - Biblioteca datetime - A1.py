# Biblioteca datetime
# Utilizada para trabalhar com datas e horas

import datetime as dt
from datetime import datetime, timedelta
import os
import random

os.system('cls')

# Exibir a data e hora
agora = datetime.now()
print('Data e hora atual:', agora, '\n')

# Converter a data para uma string
agora_str = agora.strftime('%d/%m/%Y %H:%M:%S')
print('Data formatada:', agora_str, '\n')

# Diferentes fusos horários
fuso_horario = dt.timezone(dt.timezone(hours=-3)) # Fuso de Brasilia
agora_brasilia = agora.astimezone(fuso_horario)
print('Hora de Brasilia:', agora_brasilia, '\n')

# Cálculos com datas
amanha = agora + timedelta(days=1)
print('Amanhã será:', amanha, '\n')

# Diferença entre datas
data_futura = agora + timedelta(days=random.randint(50, 150))
print('Data no futuro:', data_futura.strftime('%d/%m/%Y %H:%M:%S'), '\n')

diferanca = data_futura - agora
print('Diferença entre data futura e agora:', diferanca.days, '\n')
print('Diferença em horas:'/ diferanca.total_seconds() // 3600, '\n')
print('Diferença em meses:', diferanca.days // 30, '\n')
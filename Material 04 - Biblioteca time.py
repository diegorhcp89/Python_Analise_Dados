# Biblioteca time
# utilizada para manipulação de tempo

import time
import os

os.system('cls')

tempo = time.localtime()
print(tempo, '\n')

ano = tempo.tm_year
mes = tempo.tm_mon
dia = tempo.tm_mday
print('DD/MM/YYYY: ', dia, '/', mes, '/', ano, sep='')

hora = tempo.tm_hour
minuto = tempo.tm_min
segundo = tempo.tm_sec
print('HH:MM:SS ', hora, ':', minuto, ':', segundo, '\n', sep='')

dia_do_ano = tempo.tm_yday
dia_da_semana = tempo.tm_wday
print('Dia do ano: ', dia_do_ano, '\n', 'Dia da semana: ', dia_da_semana, '\n', sep='')

# Exibir relógio por 5 segundos

relogio_inicial = time.localtime()
relogio_em_segundos = time.mktime(relogio_inicial)
relogio_em_segundos += 5
relogio_fim = time.localtime(relogio_em_segundos)

print('HH:MM:SS - ', relogio_fim.tm_hour, ':',
      relogio_fim.tm_min, ':',
      relogio_fim.tm_sec, '\n', sep='')

# Incremento automático
while True:
    hora_local = time.localtime()
    resultado = time.strftime('%H:%M:%S %p', hora_local)
    print(resultado)
    time.sleep(1)

    if hora_local == relogio_fim:
        break

# Exemplo: Cálculo do tempo de execução de uma rotina
print('\nSimulando a execução: \n')
inicio = time.time()
for numeros in range(60):
    print(numeros)

fim = time.time()
duracao = fim - inicio
print(f'Duração: {duracao:.2f} segundos... \n')
